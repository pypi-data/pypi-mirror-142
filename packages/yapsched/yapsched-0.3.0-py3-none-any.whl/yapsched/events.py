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
"""Defines and describes the types of events that may occur in the `Scheduler`.

This includes events from both `Job`s and the `Scheduler` itself.
`Event`s are integers but can be seen as bitstring flags, such that bitwise operations
can be performed on them.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional
import traceback

EVENT_SCHEDULER_STARTED = 2 ** 0
EVENT_SCHEDULER_STOPPED = 2 ** 1
EVENT_SCHEDULER_PAUSED = 2 ** 2
EVENT_SCHEDULER_RESUMED = 2 ** 3
EVENT_ALL_JOBS_REMOVED = 2 ** 4
EVENT_JOB_ADDED = 2 ** 5
EVENT_JOB_REMOVED = 2 ** 6
EVENT_JOB_MODIFIED = 2 ** 7
EVENT_JOB_EXECUTED = 2 ** 8
EVENT_JOB_ERROR = 2 ** 9
EVENT_JOB_MISSED = 2 ** 10
EVENT_JOB_SUBMITTED = 2 ** 11
EVENT_JOB_MAX_INSTANCES = 2 ** 12
EVENT_JOB_TERMINATED = 2 ** 13

# UPDATE THIS WHENEVER AN EVENT IS ADDED/REMOVED!
# if the last event is 2 ** x, this should be 2 ** (x + 1) - 1
EVENT_ALL = 2 ** 14 - 1


@dataclass
class Event:
    """Base class to describe events.

    Attributes:
        code (int): Represents a bitstring flag.
    """
    code: int


class SchedulerEvent(Event):
    """Describes a `Scheduler` event."""
    pass


@dataclass
class JobEvent(Event):
    """Base class to describe any `Job` related event.

    Attributes:
        job_id (str): Unique identifier for this `Job`.
    """
    job_id: str


class JobExecutionEvent(JobEvent):
    """Describes the status and properties of a `Job` that was executed.

    Attributes:
        instance_id (int): The `Job`'s process instance identifier.
        run_time (datetime): The time when the `Job` was executed.
        success (bool): If the `Job` ran successfully.
        retval (Any): The return value of the `Job`'s `func`.
        exc (Exception): An exception to raise if the `Job` did not run successfully.
        formatted_exc (str): A string format version of the exception and its trace.
    """

    def __init__(self, code: int, job_id: str, instance_id: int, run_time: datetime, success: bool, retval: Any = None,
                 exc: Optional[Exception] = None) -> None:
        """Initializes a `JobExecutionEvent`.

        Args:
            code (int): A bitstring flag for this event.
            job_id (str): The `Job`'s unique identifier.
            instance_id (int): The `Job`'s process instance identifier.
            run_time (datetime): When the `Job` was executed.
            success (bool): If the `Job` executed succesfully.
            retval (Any, optional): The return value of the `Job`'s `func`. Defaults to None.
            exc (Exception, optional): An exception that was raised by the `Job`. Defaults to None.
        """
        super().__init__(code, job_id)

        self.instance_id = instance_id
        self.run_time = run_time
        self.success = success
        self.retval = retval
        self.exc = exc

        self.formatted_exc: Optional[str]
        if exc is not None:
            self.formatted_exc = ''.join(traceback.format_exception(type(exc), exc, exc.__traceback__)).rstrip()
        else:
            self.formatted_exc = None
