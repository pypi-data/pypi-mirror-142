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
"""Defines `Trigger`s that can be fired to execute jobs on a given schedule.

Two default `Trigger`s are provided:
    `DateTrigger`: Which will fire at a given date and time.
    `CronTrigger`: Which acts like a typical cron job, accepting a cron expression.
"""

from datetime import datetime
from zoneinfo import ZoneInfo
from abc import ABC, abstractmethod
import logging
from typing import Optional
from croniter import croniter
from .util import get_class_logger


class Trigger(ABC):
    """Abstract Base Class that describes types of triggers for jobs.

    Attributes:
        logger (Logger): The class' logger.
        tz (ZoneInfo): Timezone to use, set to UTC.
    """

    def __init__(self) -> None:
        self.logger: logging.Logger = get_class_logger(self)
        self.tz: ZoneInfo = ZoneInfo('UTC')

    @abstractmethod
    def get_next_fire_time(self, previous: Optional[datetime] = None, latest: Optional[datetime] = None) -> Optional[datetime]:
        """Returns the next scheduled time for the trigger to fire, if any.

        Args:
            previous (Optional[datetime]): Boundary datetime to look after.
                Defaults to None.
            latest (Optional[datetime]): Boundary datetime to look up until.
                Defaults to None.

        Returns:
            Optional[datetime]: The next scheduled time for the trigger. None if it isn't scheduled
                to be triggered.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class DateTrigger(Trigger):
    """A `Trigger` that is determined by a date and time.

    Attributes:
        run_time (datetime): When the trigger should be fired.
    """

    def __init__(self, run_time: datetime) -> None:
        """Initalizes a `DateTrigger`.

        Args:
            run_time (datetime): When the trigger should be fired.
        """
        super().__init__()
        self.run_time: datetime = run_time

    def get_next_fire_time(self, previous: Optional[datetime] = None, latest: Optional[datetime] = None) -> Optional[datetime]:
        next_fire_time: Optional[datetime]
        next_fire_time = self.run_time if previous is None or self.run_time > previous else None
        return next_fire_time

    def __getstate__(self) -> dict[str, Optional[datetime]]:
        """Returns the current state, used for pickling.

        Returns:
            dict: Dictionary mapping of `DateTrigger` attribute to value.
        """
        return {
            'run_time': self.run_time
        }

    def __setstate__(self, state: dict[str, datetime]) -> None:
        """Explicitly sets all the attributes, used for unpickling.

        Args:
            state (Dict): Mapping of `DateTrigger` attributes to their respective values.
        """
        self.run_time = state['run_time']

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} (run_time="{self.run_time}")>'

    def __str__(self) -> str:
        return f'date[{self.run_time}]'


class CronTrigger(Trigger):
    """A `Trigger` setup as a cron job.

    Attributes:
        cron_str (str): A cron expression string, five time units can be specified as follows:
            <minute> <hour> <day of month> <month> <day of week> 
    """

    def __init__(self, cron_str: str) -> None:
        """Initializes a CronTrigger.

        Args:
            cron_str (str): A cron expression string, five time units can be specified as follows:
                <minute> <hour> <day of month> <month> <day of week> 
        """
        super().__init__()
        self.cron_str: str = cron_str

    def get_next_fire_time(self, previous: Optional[datetime] = None, latest: Optional[datetime] = None) -> Optional[datetime]:
        if previous is None:
            previous = datetime.now(tz=self.tz)

        itr = croniter(self.cron_str, previous)

        next_fire_time = datetime.fromtimestamp(itr.get_next(), tz=self.tz)

        if latest is not None and next_fire_time > latest:
            return None

        return next_fire_time

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} (cron_str="{self.cron_str}")>'

    def __str__(self) -> str:
        return f'cron[{self.cron_str}]'
