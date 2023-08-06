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
"""Defines the `Job` class, the basic unit of work for the `Scheduler`.

Each `Job`, at minimum, has a unique identifier and a function to execute when it has been
scheduled to run.
"""

from typing import Any, Optional, Callable, Protocol, TypedDict, cast
from datetime import datetime
import inspect
from .triggers import Trigger
from . import util


# pylint: disable=too-few-public-methods
class JobFunction(Protocol):
    """What is called by a `Job` when run.

    Args:
        job_id (str): A unique ID for the job.
        instance_id (int): The instance id for this `Job` process.
        *args: Any additional arguments.
        **kwargs: Any additional keyword arguments.
    """
    def __call__(self,
                 job_id: str,
                 instance_id: int,
                 *args: Any,
                 **kwargs: Any) -> Any: ...

    def __self__(self) -> 'JobFunction':
        pass


class JobCallback(Protocol):
    """What is called after the `Job` executes successfully.

    Args:
        job_id (str): A unique ID for the job.
        instance_id (int): The instance id for this `Job` process.
        retval (Any): The return value from the `JobFunction`.
    """
    def __call__(self,
                 job_id: str,
                 instance_id: int,
                 retval: Any) -> None: ...


class JobErrorCallback(Protocol):
    """What is called after the `Job` fails to execute successfully.

    Args:
        job_id (str): A unique ID for the job.
        instance_id (int): The instance id for this `Job` process.
        exc (Exception): What `Exception` was raised during the `JobFunction`.
    """
    def __call__(self,
                 job_id: str,
                 instance_id: int,
                 exc: Optional[Exception]) -> None: ...


class Job:
    """A job to be executed by the executor.

    Attributes:
        func (JobFunction): The function to be called when the job executes.
        func_ref (str): Path to the `func` function, which is used for `Job` serialization.
        id (str): A unique ID of the job.
        args (Tuple): The arguments to pass to the `func`.
        kwargs (Dict): The keyword arguments to pass to the `func`.
        dynamic_args (Dict[str, Callable]): A dictionary of argument names mapping to functions that
            will be executed upon job execution. the return values of the functions will be passed
            to func as keyword arguments.
        trigger (Trigger): The trigger to used to determine when the job will execute.
        next_run_time (Optional[datetime]): The next run time of the job. If None,
            the next run time will be determined by the trigger. Defaults to None.
        description (Optional[str]): The description of the job. Defaults to None.
        coalesce (bool): If true, it will only run once when several run times are due.
            Defaults to False.
        max_instances (int): The maximum number of concurrently running instances of the
            job. -1 means no limit, 0 means disabled. Defaults to -1.
        active (bool): Determines if the job is active and should be executed.
            Defaults to True.
        callback (Optional[JobCallback]): A function to call if `func` executes successfully.
            It must accept three arguments: `job_id`, `instance_id`, and `retval`. The `retval`
            argument will be the return value of `func`. Defaults to None.
        callback_ref (str): Path to the `callback` function, which is used for `Job` serialization.
        error_callback (Optional[JobErrorCallback]): A function to call if `func` raises an
            exception. It must accept three arguments: `job_id`, `instance_id`, and `exc`.
            The `exc` argument will be the exception instance. Defaults to None.
        error_callback_ref (str): Path to the `error_callback` function, which is used for `Job`
            serialization.
    """

    def __init__(self,
                 func: JobFunction,
                 identifier: str,
                 args: tuple,
                 kwargs: dict[str, Any],
                 dynamic_args: dict[str, Callable],
                 trigger: Trigger,
                 next_run_time: Optional[datetime] = None,
                 description: Optional[str] = None,
                 coalesce: bool = False,
                 max_instances: int = -1,
                 active: bool = True,
                 callback: Optional[JobCallback] = None,
                 error_callback: Optional[JobErrorCallback] = None):
        """Initializes a `Job`.

        Args:
            func (JobFunction): The function to be called when the job executes.
            identifier (str): A unique ID of the job.
            args (Tuple): The arguments to pass to the `func`.
            kwargs (Dict): The keyword arguments to pass to the `func`.
            dynamic_args (Dict[str, Callable]): A dictionary of argument names mapping to functions
                that will be executed upon job execution. The return values of the functions will
                be passed to func as keyword arguments.
            trigger (Trigger): The trigger used to determine when the job will execute.
            next_run_time (Optional[datetime]): The next run time of the job. If None,
                the next run time will be determined by the trigger. Defaults to None.
            description (Optional[str]): The description of the job. Defaults to None.
            coalesce (bool): If true, it will only run once when several run times are
                due.  Defaults to False.
            max_instances (int): The maximum number of concurrently running instances
                of the job. -1 means no limit, 0 means disabled. Defaults to -1.
            active (bool): Determines if the job is active and should be executed.
                Defaults to True.
            callback (Optional[JobCallback]): A function to call if `func` executes
                successfully. It must accept three arguments: `job_id`, `instance_id`, and `retval`.
                The `retval` argument will be the return value of `func`. Defaults to None.
            error_callback (Optional[JobErrorCallback]): A function to call if `func` raises an
                exception. It must accept three arguments: `job_id`, `instance_id`, and `exc`.
                The `exc` argument will be the exception instance. Defaults to None.
        """
        self.func = func
        self.id = identifier
        self.args = args
        self.kwargs = kwargs
        self.trigger = trigger
        self.next_run_time = next_run_time
        self.description = description
        self.coalesce = coalesce
        self.max_instances = max_instances
        self.active = active

        self.func_ref: Optional[str]
        try:
            self.func_ref = util.obj_to_ref(self.func)
        except ValueError:
            self.func_ref = None

        self.callback: JobCallback
        if callback is None:
            self.callback = dummy_callback  # type: ignore
        else:
            self.callback = callback

        self.error_callback: JobErrorCallback
        if error_callback is None:
            self.error_callback = dummy_callback  # type: ignore
        else:
            self.error_callback = error_callback

        self.callback_ref: Optional[str]
        try:
            self.callback_ref = util.obj_to_ref(self.callback)
        except ValueError:
            self.callback_ref = None

        self.error_callback_ref: Optional[str]
        try:
            self.error_callback_ref = util.obj_to_ref(self.error_callback)
        except ValueError:
            self.error_callback_ref = None

        dynamic_arg = TypedDict('dynamic_arg', {'func': Callable[..., Any], 'func_ref': Optional[str]})
        self.dynamic_args: dict[str, dynamic_arg] = {}
        arg_func_ref: Optional[str]
        for arg_name, arg_func in dynamic_args.items():
            try:
                arg_func_ref = util.obj_to_ref(arg_func)
            except ValueError:
                arg_func_ref = None

            self.dynamic_args[arg_name] = {'func': arg_func, 'func_ref': arg_func_ref}

    def _modify(self, **changes: dict[str, Any]) -> None:
        pass

    def _get_run_times(self, latest: datetime) -> list[datetime]:
        """Returns a list of all the upcoming datetimes when the job is scheduled to run.

        Args:
            latest (datetime): Exclusionary boundary for upcoming jobs - serves as an 'up to' time.

        Returns:
            List[datetime]: A list of all the upcoming datetimes when th job is scheduled to run.
        """
        run_times: list[datetime] = []
        next_run_time = self.next_run_time
        while next_run_time and next_run_time < latest:
            run_times.append(next_run_time)
            next_run_time = self.trigger.get_next_fire_time(next_run_time, latest)
        return run_times

    def get_next_run_time_ts(self) -> Optional[float]:
        """Returns the timestamp for the next scheduled run time of the job."""
        return self.next_run_time.timestamp() if self.next_run_time is not None else None

    def __getstate__(self) -> dict[str, Any]:
        """Returns the current state of the job, used for pickling.

        Raises:
            Exception: If the `func_ref`, `callback_ref`, `error_callback_ref`, or
                `func_ref` of any `dynamic_args` is None.

        Returns:
            Dict[str, Any]: Contains a mapping of `Job` attributes to their values, except
                the function reference paths.
        """
        if self.func_ref is None:
            raise Exception(f'Job function ({self.func}) not serializable')

        if self.callback_ref is None:
            raise Exception(f'Job callback function ({self.callback}) not serializable')

        if self.error_callback_ref is None:
            raise Exception(f'Job error callback function ({self.error_callback}) not serializable')

        dynamic_args: dict[str, str] = {}
        for arg_name, values in self.dynamic_args.items():
            func = values['func']
            func_ref = values['func_ref']
            if func_ref is None:
                raise Exception(f'Job dynamic arg function ({func}) not serializable')
            dynamic_args[arg_name] = func_ref

        if inspect.ismethod(self.func) and not inspect.isclass(self.func.__self__):
            args = (self.func.__self__,) + tuple(self.args)
        else:
            args = self.args

        return {
            'id': self.id,
            'func': self.func_ref,
            'args': args,
            'kwargs': self.kwargs,
            'dynamic_args': dynamic_args,
            'trigger': self.trigger,
            'next_run_time': self.next_run_time,
            'description': self.description,
            'coalesce': self.coalesce,
            'max_instances': self.max_instances,
            'active': self.active,
            'callback': self.callback_ref,
            'error_callback': self.error_callback_ref,
        }

    def __setstate__(self, state: dict[str, Any]) -> None:
        """Explicitly sets all `Job` attributes, used when unpickling.

        Args:
            state (Dict): Mapping of `Job` attributes to their respective values.
        """
        self.id = state['id']

        self.func_ref = state['func']
        self.func = util.ref_to_obj(self.func_ref)  # type: ignore

        self.args = state['args']
        self.kwargs = state['kwargs']
        self.trigger = state['trigger']
        self.next_run_time = state['next_run_time']
        self.description = state['description']
        self.coalesce = state['coalesce']
        self.max_instances = state['max_instances']
        self.active = state['active']

        self.callback_ref = state['callback']
        self.callback = util.ref_to_obj(self.callback_ref)  # type: ignore

        self.error_callback_ref = state['error_callback']
        self.error_callback = util.ref_to_obj(self.error_callback_ref)  # type: ignore

        self.dynamic_args = {}
        for arg_name, func_ref in state['dynamic_args'].items():
            func = cast(Callable[..., Any], util.ref_to_obj(func_ref))
            func_ref = cast(Optional[str], func_ref)
            self.dynamic_args[arg_name] = {'func': func, 'func_ref': func_ref}

    def __eq__(self, other: object) -> bool:
        """`Job`s are equal when they share identical `id`s.

        Args:
            other (Any): An object to be compared against.

        Returns:
            bool: True if `other` is a `Job` and shares an identical `id`, False otherwise.
        """
        if isinstance(other, Job):
            return self.id == other.id
        raise NotImplemented

    def __repr__(self) -> str:
        return f'<Job (id={self.id})>'

    def __str__(self) -> str:
        status = f'next run at: {self.next_run_time}' if self.next_run_time is not None else 'INACTIVE'
        return f'{self.id} (trigger: {self.trigger}, {status})'


def dummy_callback(x, y, z) -> None:  # type: ignore
    pass
