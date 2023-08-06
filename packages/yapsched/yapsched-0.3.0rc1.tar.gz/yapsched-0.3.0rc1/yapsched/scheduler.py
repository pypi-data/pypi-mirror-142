# Copyright 2020 Software Factory Labs, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The main interface for this package, the `Scheduler` manages a set of `Job`s.

A `Scheduler` maintains a `JobStore` of `Job`s to run, which are run through an `Executor`. The
`Job`s are run in a multiprocessing fashion.
Listeners allow for the additional execution of methods depending on `Scheduler` or `Job`
`Event`s.

The `Scheduler` is run on a thread with its `_main_loop` method.
"""

from enum import Enum, auto
from typing import Any, ClassVar, Optional, Callable
import threading
import uuid
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import logging
import zoneinfo
from .job import Job, JobFunction, JobCallback, JobErrorCallback
from . import executor, triggers, events
from .jobstores import JobDoesNotExistException, JobStore, memory

logger = logging.getLogger(__name__)


class State(Enum):
    """Enum describing the state of the `Scheduler`."""
    STOPPED = auto()
    RUNNING = auto()
    PAUSED = auto()


class Scheduler:
    """Manages the execution of provided Jobs via their respective scheduled triggers.

    The `Scheduler` has three states:
    * RUNNING
    * PAUSED
    * STOPPED

    Each `Job` can be added or removed from the provided `JobStore`, or modified in place.
    Listeners allow for certain actions to be taken when `Scheduler` or `Job` events occur.

    Attributes:
        _executor (executor.Executor): Handles the execution of Jobs.
        _executor_lock (threading.RLock): Reentrant lock to control access to the `_executor`.
        _jobstore (Optional[jobstores.JobStore]): JobStore for the Scheduler's jobs.
            Defaults to None.
        _jobstore_lock (threading.RLock): Reentrant lock to control access to the `_jobstore`.
        _listeners (List[Tuple(Callable, int)]): List of functions to be called upon a certain
            event occuring.
        _listeners_lock (threading.RLock): Reentrant lock to control access to the `_listeners`.
        state (State): Describes the Scheduler's current state.
        tz (zoneinfo): The timezone for the Scheduler to operate in. Defaults to
            timezone.utc.
    """
    _event: ClassVar[threading.Event]
    _thread: ClassVar[threading.Thread]

    @classmethod
    def set_thread(cls, thread: threading.Thread) -> None:
        """Sets the class `_thread` variable."""
        cls._thread = thread

    @classmethod
    def set_event(cls) -> None:
        """Sets the class `_event` variable."""
        cls._event = threading.Event()

    def __init__(self, pool_size: int = 10, jobstore: Optional[JobStore] = None, tz: zoneinfo = ZoneInfo('UTC')) -> None:
        """Initializes the `Scheduler`.

        Args:
            pool_size (int): Determines the pool size for the job `Executor`. Defaults
                to 10.
            jobstore (Optional[jobstores.JobStore]): A `JobStore` to manage the `Scheduler`'s
                `Job`s. Defaults to None.
            tz (zoneinfo): The timezone for the `Scheduler` to operate in. Defaults to
                timezone.utc.

        Raises:
            ValueError: If the provided timezone is None.
        """
        if tz is None:
            raise ValueError('tz must not be None')

        self._executor = executor.Executor(pool_size, self)
        self._executor_lock = threading.RLock()

        self._jobstore_lock = threading.RLock()

        self._listeners: list[tuple[Callable[[events.Event], None], int]] = []
        self._listeners_lock = threading.RLock()

        self.state = State.STOPPED

        self.tz: zoneinfo = tz

        self.configure(jobstore=jobstore, tz=tz)

    def configure(self, jobstore: Optional[JobStore] = None, tz: zoneinfo = None) -> None:
        """Configures the `_jobstore` and `tz` after initialization.

        Args:
            jobstore (Optional[jobstores.JobStore]): `JobStore` for the `Scheduler`'s `Job`s.
                Defaults to None.
            tz (zoneinfo): The timezone for the `Scheduler` to operate in.
        """
        if jobstore is None:
            jobstore = memory.MemoryJobStore()

        jobstore._scheduler = self
        self._jobstore = jobstore

        if tz is not None:
            self.tz = tz

    def start(self, paused: bool = False) -> None:
        """Starts the `Scheduler`.

        Args:
            paused (bool): Determines if the `Scheduler` should start paused or running.
                Defaults to False.

        Raises:
            SchedulerAlreadyRunningException: If the `Scheduler` is already running.
        """
        if self.state != State.STOPPED:
            raise SchedulerAlreadyRunningException

        self.set_event()

        with self._executor_lock:
            self._executor.setup()

        with self._jobstore_lock:
            self._jobstore.setup()

        self.add_listener(self._internal_listener)

        self.state = State.PAUSED if paused else State.RUNNING
        logger.info('Scheduler started')
        self._dispatch_event(events.SchedulerEvent(events.EVENT_SCHEDULER_STARTED))

        if not paused:
            self.wakeup()

        thread = threading.Thread(target=self._main_loop, name='yapsched', daemon=True, args=(self._event,))
        self.set_thread(thread)
        self._thread.start()

    def shutdown(self, wait: bool = True) -> None:
        """Shuts down the `Scheduler`.

        Args:
            wait (bool): Determines if it should wait for `Job` processes to stop.
                Defaults to True.

        Raises:
            SchedulerNotRunningException: If the `Scheduler` is not running.
        """
        if self.state == State.STOPPED:
            raise SchedulerNotRunningException

        logger.info('Shutting down...')

        self.state = State.STOPPED

        logger.debug('Closing thread')
        self._event.set()
        self._thread.join()

        logger.debug('Deleting thread')
        delattr(Scheduler, '_thread')

        logger.debug('Tearing down executor')
        with self._executor_lock:
            self._executor.teardown(wait)

        logger.debug('Tearing down jobstore')
        with self._jobstore_lock:
            self._jobstore.teardown()

        self._dispatch_event(events.SchedulerEvent(events.EVENT_SCHEDULER_STOPPED))

        self.remove_listener(self._internal_listener)

        logger.info('Scheduler shutdown')

    def pause(self) -> None:
        """Pauses the `Scheduler`.

        Raises:
            SchedulerNotRunningException: If the `Scheduler` is not running.
        """
        if self.state == State.STOPPED:
            raise SchedulerNotRunningException
        elif self.state == State.RUNNING:
            self.state = State.PAUSED
            logger.info('Scheduler paused')
            self._dispatch_event(events.SchedulerEvent(events.EVENT_SCHEDULER_PAUSED))

    def resume(self) -> None:
        """Resumes the `Scheduler`.

        Raises:
            SchedulerNotRunningException: If the `Scheduler` is stopped.
        """
        if self.state == State.STOPPED:
            raise SchedulerNotRunningException
        elif self.state == State.PAUSED:
            self.state = State.RUNNING
            logger.info('Scheduler resumed')
            self._dispatch_event(events.SchedulerEvent(events.EVENT_SCHEDULER_RESUMED))
            self.wakeup()

    @property
    def running(self) -> bool:
        """bool: Determines if the `Scheduler` is currently running (RUNNING or PAUSED)."""
        return self.state != State.STOPPED

    def wakeup(self) -> None:
        """Wakes the `Scheduler` up to process events."""
        self._event.set()

    def add_job(self,
                func: JobFunction,
                args: Optional[tuple] = None,
                kwargs: Optional[dict[str, Any]] = None,
                dynamic_args: Optional[dict[str, Callable]] = None,
                identifier: Optional[str] = None,
                description: Optional[str] = None,
                coalesce: bool = False,
                max_instances: int = -1,
                replace_existing: bool = False,
                trigger: Optional[triggers.Trigger] = None,
                next_run_time: Optional[datetime] = None,
                active: bool = True,
                callback: Optional[JobCallback] = None,
                error_callback: Optional[JobErrorCallback] = None) -> Job:
        """Adds a `Job` to the `Jobstore`.

        Args:
            func (JobFunction): The function to be called when the job executes.
            args (Optional[List]): The arguments to pass to the `func`. Defaults to None.
            kwargs (Optional[Dict]): The keyword arguments to pass to the `func`. Defaults to None.
            dynamic_args (Optional[Dict[str, Callable]]): A dictionary of argument names mapping to
                functions that will be executed upon job execution. The return values of the
                functions will be passed to func as keyword arguments. Defaults to None.
            identifier (Optional[str]): A unique ID for the job. Defaults to None.
            description (Optional[str]): The description of the job. Defaults to None.
            coalesce (bool): If true, it will only run once when several run timnes are due.
                Defaults to False.
            max_instances (int): The maximum number of concurrently running instances of the job.
                -1 means no limit, 0 means disabled. Defaults to -1.
            replace_existing (bool): Determines if a currently existing job of this id should be
                replaced.  Defaults to False.
            trigger (Optional[triggers.Trigger]): The trigger used to determine when the job will
                execute. Defaults to None.
            next_run_time (Optional[datetime]): When the job should run next. Defaults to None.
            active (bool): If the job should be marked as active. Defaults to True.
            callback (Optional[JobCallback]): A function to call if `func` executes
                successfully. It must accept three arguments: `job_id`, `instance_id`, and `retval`.
                The `retval` argument will be the return value of `func`. Defaults to None.
            error_callback (Optional[JobErrorCallback]): A function to call if `func` raises an
                exception. It must accept three arguments: `job_id`, `instance_id`, and `exc`.
                The `exc` argument will be the exception instance. Defaults to None.

        Raises:
            ValueError: If there is no next run time and the `Job` isn't active.

        Returns:
            Job: An instance of the `Job` created by the provided arguments.
        """
        if next_run_time is not None and not active:
            raise ValueError('Job can\'t be inactive and have a non-null next_run_time!')

        if identifier is None:
            identifier = str(uuid.uuid4())

        if trigger is None:
            trigger = triggers.DateTrigger(datetime.now(tz=self.tz))

        trigger.tz = self.tz

        job = Job(func,
                  identifier,
                  tuple(args) if args is not None else (),
                  kwargs if kwargs is not None else {},
                  dynamic_args if dynamic_args is not None else {},
                  trigger,
                  next_run_time=next_run_time,
                  description=description,
                  coalesce=coalesce,
                  max_instances=max_instances,
                  active=active,
                  callback=callback,
                  error_callback=error_callback)

        with self._jobstore_lock:
            self._jobstore.add_job(job, replace_existing)

        logger.info(f'Added job {identifier}')
        self._dispatch_event(events.JobEvent(events.EVENT_JOB_ADDED, identifier))

        if self.state == State.RUNNING and active:
            self.wakeup()

        return job

    def modify_job(self, job_id: str, **changes: Any) -> Job:
        """Modifies the `Job` with the given `job_id`.

        Changes is a dictionary containing mappings of `Job` attributes
        to new values.

        Args:
            job_id (str): Identifier for the `Job` to modify.
            **changes (dict[str, Any]): Keyword arguments to modify the job with.
        Raises:
            ValueError: If the newly provided next run time is None and the `Job` is not active.

        Returns:
            Job: The `Job` instance after being updated.
        """
        with self._jobstore_lock:
            job = self.get_job(job_id)

            new_next_run_time: Optional[datetime] = changes.get('next_run_time', None)

            if new_next_run_time and not isinstance(new_next_run_time, datetime):
                raise ValueError(f'Expected changes["next_run_time"] to be a datetime, but got '
                                 f'{type(new_next_run_time)}')
            elif new_next_run_time is None:
                new_next_run_time = job.next_run_time

            new_active: Optional[bool] = changes.get('active', None)

            if new_active and not isinstance(new_active, bool):
                raise ValueError(f'Expected changes["active"] to be a bool, but got '
                                 f'{type(new_active)}')
            elif new_active is None:
                new_active = job.active

            if new_next_run_time is not None and not new_active:
                raise ValueError('Job can\'t be inactive and have a non-null next_run_time!')

            job._modify(**changes)

            if job.trigger is None:
                job.trigger = triggers.DateTrigger(datetime.now(tz=self.tz))

            job.trigger.tz = self.tz

            self._jobstore.update_job(job)

        self._dispatch_event(events.JobEvent(events.EVENT_JOB_MODIFIED, job_id))

        if self.state == State.RUNNING:
            self.wakeup()

        return job

    def get_job(self, job_id: str) -> Job:
        """Returns the `Job` with the given `job_id`.

        Args:
            job_id (str): The identifier for the `Job` to get.

        Returns:
            Job: The `Job` associated with the given `job_id`.
        """
        with self._jobstore_lock:
            return self._jobstore.get_job(job_id)

    def get_jobs(self, pattern: str = None) -> list[Job]:
        """Returns all `Job`s.

        Args:
            pattern (str, optional): A regular expression pattern to match `Job` ids against.
                Defaults to None.

        Returns:
            List[Job]: A list of all the `Job`s.
        """
        with self._jobstore_lock:
            return self._jobstore.get_jobs(pattern)

    def remove_job(self, job_id: str) -> None:
        """Removes a single `Job` instance.

        Args:
            job_id (str): The identifier for the `Job` to remove.
        """
        with self._jobstore_lock:
            self._jobstore.remove_job(job_id)

        logger.info(f'Removed job {job_id}')
        self._dispatch_event(events.JobEvent(events.EVENT_JOB_REMOVED, job_id))

    def terminate_job(self, instance_id: int) -> None:
        """Terminates a single `Job` instance.

        Args:
            instance_id (int): The instance id for the `Job`.
        """
        with self._executor_lock:
            job_id = self._executor.terminate_job(instance_id)
            logger.info(f'Terminated job {job_id}')
            self._dispatch_event(events.JobEvent(events.EVENT_JOB_TERMINATED, job_id))

    def trigger_job(self, job_id: str) -> int:
        """Triggers a `Job` to run immediately.

        Args:
            job_id (str): The identifier for the `Job` to trigger.

        Returns:
            int: The instance id for the `Job`'s execution.
        """
        job = self.get_job(job_id)
        run_time = datetime.now(tz=self.tz)

        try:
            instance_id = self._executor.submit_job(job, run_time)
        except executor.MaxJobInstancesReachedException:
            self._dispatch_event(events.JobEvent(events.EVENT_JOB_MAX_INSTANCES, job_id))
            raise

        return instance_id

    def get_job_instance_ids(self, job_id: str) -> list[int]:
        """Returns the instance ids for the given `Job`.

        Args:
            job_id (str): The identifier for the `Job` with running instances.

        Raises:
            jobstores.JobDoesNotExistException: If the `Job` does not currently exist.

        Returns:
            List[int]: A list of instance ids associated with the given `job_id`.
        """
        with self._jobstore_lock:
            if not self._jobstore.contains_job(job_id):
                raise JobDoesNotExistException(job_id)

        with self._executor_lock:
            return self._executor.get_job_instance_ids(job_id)

    def get_job_with_instance_id(self, instance_id: int) -> Job:
        """Returns the `Job` associated with the given instance id.

        Args:
            instance_id (int): The id for the instance we're interested in.

        Returns:
            Job: The `Job` associated with the given instance id.
        """
        with self._executor_lock:
            return self._executor.get_job(instance_id)

    def get_running_jobs(self) -> list[executor.Instance]:
        """Returns a list of all `Job`s that are currently running.

        Returns:
            List[dict]: A List of dictionaries correlating a `Job` with its instance information.
            Each dictionary will be of the following format:
            {
                'job': <Job Instance>
                'id': <Instance's id>
                'start_time': <Datetime>
                'process': <Process instance>
            }
        """
        with self._executor_lock:
            return self._executor.get_instances()

    def add_listener(self, callback: Callable[[events.Event], None], mask: int = events.EVENT_ALL) -> None:
        """Adds a listener for an event.

        Args:
            callback (Callable): A function to call upon an event.
            mask (int, optional): Serves as a bitwise mask for the interested events. Defaults to
                events.EVENT_ALL.
        """
        with self._listeners_lock:
            self._listeners.append((callback, mask))

    def remove_listener(self, callback: Callable[[events.Event], None]) -> None:
        """Removes a listener.

        Args:
            callback (function): Used to find the listener to remove, if their callback functions
                match.
        """
        with self._listeners_lock:
            for i, (cb, _) in enumerate(self._listeners):
                if callback == cb:
                    del self._listeners[i]

    def _main_loop(self, event) -> None:
        """Processes the submitted `Job`s, unless in a non-running state."""
        max_wait = threading.TIMEOUT_MAX
        wait_seconds = max_wait
        while self.state != State.STOPPED:
            event.wait(wait_seconds)
            event.clear()
            if self.state == State.STOPPED:
                break
            wait_seconds = self._process_jobs()
            if wait_seconds == -1:
                wait_seconds = max_wait

    def _process_jobs(self) -> int:
        """Processes each `Job` that is currently due to run.

        After each `Job` execution its next scheduled run time is updated, or
        removed if it has none.

        Events produced by the `Job` executions also execute any requested listener
        callback functions.

        Returns:
            int: The number of seconds to wait until next wakeup.
        """
        if self.state == State.PAUSED:
            logger.debug('Scheduler paused; not processing jobs')
            return -1

        logger.info('Waking up to process jobs')
        now_dt = datetime.now(tz=self.tz)
        next_wakeup_time: Optional[datetime] = None
        events_to_dispatch = []

        with self._jobstore_lock:
            try:
                due_jobs = self._jobstore.get_due_jobs(now_dt)
                logger.debug(f'Due jobs: {due_jobs}')

                for job in due_jobs:
                    run_times = job._get_run_times(now_dt)
                    run_times = run_times[-1:] if job.coalesce else run_times
                    logger.debug(f'Job: {job}; run times: {run_times}')

                    for run_time in run_times:
                        try:
                            self._executor.submit_job(job, run_time)
                        except executor.MaxJobInstancesReachedException as e:
                            logger.error(f'Execution of job skipped: {e}')
                            events_to_dispatch.append(events.JobEvent(events.EVENT_JOB_MAX_INSTANCES, job.id))
                        except Exception as e:
                            logger.exception(e)
                        else:
                            events_to_dispatch.append(events.JobEvent(events.EVENT_JOB_SUBMITTED, job.id))

                    job_next_run_time = job.trigger.get_next_fire_time(run_times[-1], None)
                    logger.debug(f'Job next run time: {job_next_run_time}')
                    if job_next_run_time:
                        job.next_run_time = job_next_run_time
                        self._jobstore.update_job(job)
                    else:
                        self.remove_job(job.id)
            except Exception as e:
                logger.warning(f'Error getting due jobs from job store: {e}')
                next_wakeup_time = now_dt + timedelta(seconds=5)

            jobstore_next_run_time = self._jobstore.get_next_run_time()
            logger.debug(f'Jobstore next run time: {jobstore_next_run_time}')
            if jobstore_next_run_time is not None and next_wakeup_time is None:
                next_wakeup_time = jobstore_next_run_time

        for event in events_to_dispatch:
            self._dispatch_event(event)

        if self.state == State.PAUSED:
            wait_seconds = -1
            logger.debug('Scheduler is paused; waiting for resume')
        elif next_wakeup_time is None:
            wait_seconds = -1
            logger.debug('No jobs; waiting until a job is added')
        else:
            next_wakeup_time_sec = max((next_wakeup_time - now_dt).total_seconds(), 0)
            wait_seconds = min(int(next_wakeup_time_sec), int(threading.TIMEOUT_MAX))
            logger.debug(f'Next wakeup is due at {next_wakeup_time} (in {wait_seconds} seconds)')

        return wait_seconds

    def _dispatch_event(self, event: events.Event) -> None:
        """Given an event, execute any matching listener callbacks.

        Args:
            event (events.Event): The event that occurred.
        """
        with self._listeners_lock:
            listeners = tuple(self._listeners)

        for callback, mask in listeners:
            if event.code & mask:
                try:
                    callback(event)
                except Exception as e:
                    logger.error('Error notifying listener')
                    logger.exception(e)

    def _internal_listener(self, event: events.Event) -> None:
        """Internal `Scheduler` listener to watch for certain events.

        Args:
            event (events.Event): The event that occurred.
        """
        if isinstance(event, events.JobExecutionEvent):
            if event.code == events.EVENT_JOB_EXECUTED:
                with self._jobstore_lock:
                    logger.info(f'Next wakeup time: {self._jobstore.get_next_run_time()}')


class SchedulerAlreadyRunningException(Exception):
    """Raised when the `Scheduler` is already running."""
    def __init__(self) -> None:
        super().__init__('Scheduler is already running')


class SchedulerNotRunningException(Exception):
    """Raised when the `Scheduler` is not running."""
    def __init__(self) -> None:
        super().__init__('Scheduler is not running')


class JobAlreadyExistsException(Exception):
    """Raised when a `Job`'s unique ID already exists."""

    def __init__(self, job_id: str) -> None:
        """Initializes a JobAlreadyExistsException.

        Args:
            job_id (str): The job identifier that already exists.
        """
        super().__init__(f'Job already exists with ID {job_id}')
        self.job_id = job_id
