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
"""Defines the `Executor` class, which manages the execution of `Job`s.
This is built upon Python's `multiprocessing` module."""

import multiprocessing
from multiprocessing.context import SpawnProcess
from queue import Empty
from threading import Thread
from typing import Any, Callable, Optional, TYPE_CHECKING, ValuesView
from datetime import datetime
from collections import defaultdict
from dataclasses import asdict, dataclass
import random
import logging
import contextlib
from .job import Job
from . import events

if TYPE_CHECKING:
    from .scheduler import Scheduler

random.seed()
logger = logging.getLogger(__name__)

def _require_running(func: Callable[..., Any]) -> Any:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        executor: Executor = args[0]

        if not executor.is_running():
            raise ExecutorNotSetupException()

        return func(*args, **kwargs)

    return wrapper


@dataclass
class Instance:
    """Class for correlating a `Job` and its process information.

    Attributes:
        job (Job): A `Job` instance.
        id (int): A unique identifier.
        start_time (datetime): When this `Job` instance started.
        process (multiprocessing.SpawnProcess): The associated process with this instance.
    """
    job: Job
    id: int
    start_time: datetime
    process: SpawnProcess


class Executor:
    """Manages the execution of `Job`s by utilizing multiprocessing.

    Attributes:
        _pool_size (int): The number of `Job` processes executing. NOTE: Currently unutilitzed.
        _scheduler (Scheduler): The `Scheduler` which manages this `Executor`.
        _instances (Dict[int, Instance]): Mapping of process instance ids to `Job` process information.
            Instance ids are a way to associate a running `Job` with its process and start time.
        _event_queue (multiprocessing.Queue): Queue for communicating events across processes.
        _event_thread (threading.Thread): Thread that handles the `_event_queue`.
        _running (bool): Tracks the current running state.
        _lock (threading.RLock): A Reentrant lock to handle access to process instances.
        mp_ctx (multiprocessing.SpawnContext): The multiprocessing context to use, namely `Spawn`.
    """

    def __init__(self, pool_size: int, scheduler: 'Scheduler') -> None:
        """Initializes an `Executor`.

        Args:
            pool_size (int): The number of `Job` processes executing. NOTE: Currently unutilitzed.
            scheduler (Scheduler): The `Scheduler` which manages this `Executor`.
        """
        self._pool_size = pool_size  # TODO: use _pool_size
        self._scheduler = scheduler

        self._instances: dict[int, Instance] = {}
        self._jobs_to_instances: dict[str, list[int]] = defaultdict(list)

        self.mp_ctx = multiprocessing.get_context('spawn')

        if TYPE_CHECKING:
            # pylint: disable=unsubscriptable-object
            self._event_queue: Optional[multiprocessing.Queue[events.JobExecutionEvent]] = None
        else:
            self._event_queue: Optional[multiprocessing.Queue] = None

        self._event_thread: Optional[Thread] = None
        self._running = False

        self._lock = self.mp_ctx.RLock()

    def setup(self) -> None:
        """Performs basic setup functions, also starts watching the `_event_queue`.

        The `_event_thread` is ran as a daemon thread.
        """
        if self._running:
            return

        self._event_queue = self.mp_ctx.Queue()

        self._event_thread = Thread(target=self._event_read_loop, daemon=True)
        self._running = True
        self._event_thread.start()

    @_require_running
    def teardown(self, wait: bool = True) -> None:
        """Shuts down `Job` processes and cleans up the `_event_queue`.

        Args:
            wait (bool, optional): Determines if it should wait for processes to finish shutting down.
                Defaults to True.
        """
        logger.debug('Tearing down...')

        processes = [instance.process for instance in self._instances.values()]
        logger.debug(f'Processes: {processes}')

        def get_alive_procs() -> list[SpawnProcess]:
            procs = []
            for proc in processes:
                try:
                    if proc.is_alive():
                        procs.append(proc)
                except ValueError:
                    pass
            return procs

        while alive_processes := get_alive_procs():
            logger.debug(f'Alive processes: {alive_processes}')
            for process in alive_processes:
                logger.debug(f'Process: {process}')
                if not wait:
                    logger.debug('    terminating')
                    process.terminate()
                logger.debug('    joining')
                process.join(1)
                if not process.is_alive():
                    logger.debug('    closing')
                    try:
                        process.close()
                    except ValueError:
                        pass
                else:
                    logger.debug('    still alive; will try again soon')

        self._instances.clear()
        self._jobs_to_instances.clear()

        logger.debug('Closing event thread')
        self._running = False

        if self._event_thread is not None:
            self._event_thread.join()
            logger.debug('Deleting event thread')
            del self._event_thread

        logger.debug('Closing event queue')

        if self._event_queue is not None:
            self._event_queue.close()
            self._event_queue.join_thread()

        logger.debug('Done')

    @_require_running
    def submit_job(self, job: Job, run_time: datetime) -> int:
        """Submits a `Job` to be executed.

        Args:
            job (Job): A `Job` instance to execute.
            run_time (datetime): When the `Job` is scheduled to run.

        Raises:
            ExecutorNotSetupException: If `setup()` was not run.
            MaxJobInstancesReachedException: If the `Job` already has reached the maximum amount of
                instances allowed to run at one time.

        Returns:
            int: The instance id of the `Job`.
        """
        with self._lock:
            if job.max_instances != -1 and len(self._jobs_to_instances[job.id]) >= job.max_instances:
                raise MaxJobInstancesReachedException(job, self._jobs_to_instances[job.id])

            dynamic_args: dict[str, Any] = {}
            for arg_name, values in job.dynamic_args.items():
                func = values['func']
                dynamic_args[arg_name] = func()

            instance_id = self._scheduler._jobstore.get_new_instance_id()
            process = self.mp_ctx.Process(target=run_job, name=f'Process-{instance_id}',
                                          args=(job, instance_id, run_time, self._event_queue),
                                          kwargs={**job.kwargs, **dynamic_args})

            self._instances[instance_id] = Instance(job,
                                                    instance_id,
                                                    datetime.now(tz=self._scheduler.tz),
                                                    process)
            self._jobs_to_instances[job.id].append(instance_id)

            try:
                logger.info(f'Running job "{job.id}" (scheduled at {run_time})')

                with contextlib.redirect_stdout(None), contextlib.redirect_stderr(None):
                    process.start()
            except Exception:
                self._job_cleanup(job.id, instance_id, terminate=True)
                raise

            return instance_id

    @_require_running
    def terminate_job(self, instance_id: int) -> str:
        """Terminates a `Job` via its `instance_id`.

        Args:
            instance_id (int): The instance id of the desired `Job` to terminate.

        Raises:
            JobInstanceNotFoundException: If there is no instance id matching the one provided.

        Returns:
            str: The `Job`'s id that was terminated.
        """
        with self._lock:
            instance = self._instances.get(instance_id, None)

            if instance is None:
                raise JobInstanceNotFoundException(instance_id)

        job_id = instance.job.id
        self._job_cleanup(job_id, instance_id, terminate=True)

        return job_id

    @_require_running
    def get_job_instance_ids(self, job_id: str) -> list[int]:
        """Returns all instance ids associated with the provided `job_id`.

        Args:
            job_id (str): Identifier for the interested job.

        Returns:
            List[int]: A list containing all instance ids associated with the provided 'job_id'.
        """
        with self._lock:
            return self._jobs_to_instances.get(job_id, [])

    @_require_running
    def get_job(self, instance_id: int) -> Job:
        """Returns the `Job` associated with the provided `instance_id`.

        Args:
            instance_id (int): Instance id used to find the associated `Job`.

        Raises:
            JobInstanceNotFoundException: If the provided `instance_id` was not found.

        Returns:
            Job: A `Job` associated with the provided `instance_id`.
        """
        with self._lock:
            instance = self._instances.get(instance_id, None)
            if instance is None:
                raise JobInstanceNotFoundException(instance_id)

            return instance.job

    @_require_running
    def get_instances(self) -> list[Instance]:
        """Returns all instances and their associated data.

        Returns:
            list[dict]: A list of `Instance`s containing all instances and their associated data.
            Each Instance has the following data:
            {
                'job': <Job Instance>
                'id': <Instance's id>
                'start_time': <Datetime>
                'process': <Process instance>
            }
        """
        with self._lock:
            return list(self._instances.values())

    def is_running(self) -> bool:
        """Returns if the Executor is currently running.

        Returns:
            bool: True when the Executor is running, False otherwise.
        """
        return self._running

    @_require_running
    def _event_read_loop(self) -> None:
        """Processes events as they are put into the `_event_queue`.

        Upon a successful event, the `Job`'s `callback` is called.
        Upon an unsuccessful event, the `Job`'s `error_callback` is called.

        The events are passed along to the scheduler to handle as well.
        """
        logger.debug('waiting for event...')
        if self._event_queue is None:
            raise ExecutorNotSetupException()

        while self._running:
            try:
                event = self._event_queue.get(timeout=0.2)
            except Empty:
                continue

            job = self._instances[event.instance_id].job

            logger.debug(f'got event ({event}) from job {job.id}:{event.instance_id}; '
                         f'event queue size: {self._event_queue.qsize()}')

            if event.success:
                logger.info(f'Job "{job.id}" executed successfully')
                if job.callback:
                    try:
                        job.callback(job.id, event.instance_id, event.retval)
                    except Exception as e:
                        logger.error(f'callback failed!')
                        logger.exception(e)
            else:
                logger.error(f'Job "{job.id}" raised an exception\n{event.formatted_exc}')
                if job.error_callback:
                    try:
                        job.error_callback(job.id, event.instance_id, event.exc)
                    except Exception as e:
                        logger.error(f'error callback failed!')
                        logger.exception(e)

            self._job_cleanup(event.job_id, event.instance_id)
            self._scheduler._dispatch_event(event)

            logger.debug('waiting for event...')

    @_require_running
    def _job_cleanup(self, job_id: str, instance_id: int, terminate: bool = False) -> None:
        """Cleans up a `Job` instance, shutting it down if necessary and requested.

        Args:
            job_id (str): The id for the `Job` to cleanup.
            instance_id (int): The instance id for the `Job` to cleanup.
            terminate (bool, optional): Determines if the `Job` should be terminated.
                Defaults to False.
        """
        with self._lock:
            process = self._instances[instance_id].process

            logger.debug(f'cleaning up instance (job_id: {job_id}, instance_id: {instance_id}, process: {process})')

            if process.is_alive():
                if terminate:
                    logger.debug(f'terminating process')
                    try:
                        process.terminate()
                    except Exception as e:
                        logger.exception(e)
                process.join(timeout=2)

            if not process.is_alive():
                process.close()
                logger.debug('process closed')
            else:
                logger.error('Could not terminate process')

            logger.debug(f'instances: {self._instances}')
            logger.debug(f'mapping: {dict(self._jobs_to_instances)}')

            logger.debug('removing instance')
            del self._instances[instance_id]
            self._jobs_to_instances[job_id].remove(instance_id)

            logger.debug(f'instances: {self._instances}')
            logger.debug(f'mapping: {dict(self._jobs_to_instances)}')

            still_running = [f'{jid}:{str(iids).replace(" ", "")}' for jid, iids in self._jobs_to_instances.items() if iids]
            logger.info(f'Currently running: {", ".join(still_running)}')

            logger.debug('cleaned up')


def run_job(job: Job, instance_id: int, run_time: datetime, event_queue: multiprocessing.Queue, **kwargs: Any) -> None:
    """Executes the provided `Job` by running its `func`.

    Args:
        job (Job): The `Job` to run.
        instance_id (int): The instance id associated with the `job`.
        run_time (datetime): When the `job` is scheduled to run.
        event_queue (multiprocessing.Queue): Used to track the event produced by running the `job`.
    """
    try:
        retval = job.func(job.id, instance_id, *job.args, **job.kwargs, **kwargs)
        logger.debug(f'job {job.id}:{instance_id} returned {retval}')
    except Exception as e:
        logger.debug(f'job {job.id}:{instance_id} raised an exception')
        event = events.JobExecutionEvent(events.EVENT_JOB_EXECUTED, job.id, instance_id, run_time, success=False,
                                         exc=e)
    else:
        logger.debug(f'job {job.id}:{instance_id} executed successfully')
        event = events.JobExecutionEvent(events.EVENT_JOB_EXECUTED, job.id, instance_id, run_time, success=True,
                                         retval=retval)

    logger.debug(f'sending event to queue ({job.id}:{instance_id})')
    for handler in logger.handlers:
        handler.flush()
    event_queue.put(event)
    logger.debug(f'event queue size: {event_queue.qsize()} ({job.id}:{instance_id})')


class ExecutorNotSetupException(Exception):
    """Raised when the `Executor` was not setup yet."""
    def __init__(self) -> None:
        super().__init__('Executor not setup')


class MaxJobInstancesReachedException(Exception):
    """Raised when trying to run a `Job` already running the maximum number of instances.""" 

    def __init__(self, job: Job, instance_ids: list[int]) -> None:
        """Initializes a MaxJobInstancesReachedException.

        Args:
            job (Job): The `Job` which is already running the maximum number of instances.
            instance_ids (List[int]): The list of the `Job`'s instance ids.
        """
        super().__init__(f'Job "{job.id}" has already reached its maximum number of instances '
                         f'({job.max_instances})')
        self.job = job
        self.instance_ids = instance_ids


class JobInstanceNotFoundException(Exception):
    """Raised when the provided instance id was not associated with any `Job`."""

    def __init__(self, instance_id: int) -> None:
        """Initializes a JobInstanceNotFoundException.

        Args:
            instance_id (int): The instance id of which no `Job` was associated with.
        """
        super().__init__(f'Job instance {instance_id} not found')
        self.instance_id = instance_id
