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
"""Defines a `JobStore` that utilizes an SQLAlchemy database.
This allows for persistent data storage.

Two tables are utilized:
* `yapsched_jobs`: Stores `Job` data.
* `yapsched_last_instance_id: Stores the last instance id used.

It utilizes Python's `pickle` module to serialize `Job` data before inserting into the database."""

from decimal import Decimal
from typing import Any, Callable, Optional, TypeVar, cast
from datetime import datetime
import pickle
import re
from sqlalchemy import create_engine, Column, Unicode, Float, LargeBinary, Integer
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from . import JobStore, JobDoesNotExistException, JobAlreadyExistsException
from ..job import Job


Base = declarative_base()
SessionCls = scoped_session(sessionmaker())

F = TypeVar('F', bound=Callable[..., Any])  # pylint: disable=invalid-name

def db_user(func: F) -> F:
    """Wrapper function to either utilize an SQLAlchemy session or create a new one.

    Args:
        func (F): Wrapped to function to call after setting up the session.
    """
    def wrapper(self: 'SqlAlchemyJobStore', *args: Any, **kwargs: Any) -> Any:
        session: Optional[Session] = kwargs.get('session', None)
        session_exists = True

        if session is None:
            session = SessionCls()
            kwargs['session'] = session
            session_exists = False

        result = func(self, *args, **kwargs)

        if not session_exists:
            session.commit()
            session.close()

        return result
    return cast(F, wrapper)


class DbJob(Base):
    """Defines an SQLAlchemy table for `Job`s and maps onto it."""
    __tablename__ = 'yapsched_jobs'

    id = Column(Unicode(191, _warn_on_bytestring=False), primary_key=True)
    next_run_time = Column(Float(25), index=True)
    job_state = Column(LargeBinary, nullable=False)


class LastInstanceId(Base):
    """Defines an SQLAlchemy table for the `Scheduler`'s last instance id and maps onto it."""
    __tablename__ = 'yapsched_last_instance_id'

    row = Column(Integer, primary_key=True)
    id = Column(Integer)


class SqlAlchemyJobStore(JobStore):
    """A `JobStore` that utilizes an SQLAlchemy database.

    Attributes:
        pickle_protocol (int): Determines what protocol version to use when pickling.
        engine (Engine): The SQLAlchemy engine to utilize for the database.
    """

    def __init__(self, url: str = None, engine: Engine = None, engine_options: Optional[dict] = None,
                 pickle_protocol: int = pickle.HIGHEST_PROTOCOL) -> None:
        """Initializes a `SQLAlchemyJobStore`.

        Either `url` or `engine` must be defined to establish an `Engine` for SQL Alchemy to use.

        Args:
            url (str, optional): The database URL used to create an `Engine`. Defaults to None.
            engine (Engine, optional): An `Engine` used by SQLAlchemy. Defaults to None.
            engine_options (Optional[Dict]): Options used to create an `Engine` if
                `engine` is None. Defaults to None.
            pickle_protocol (int, optional): Determines what protocol version to use when pickling.
                Defaults to pickle.HIGHEST_PROTOCOL.

        Raises:
            ValueError: If both the `url` and `engine` are undefined.
        """
        super().__init__()
        self.pickle_protocol = pickle_protocol

        if engine is not None:
            self.engine = engine
        elif url is not None:
            self.engine = create_engine(url, **(engine_options or {}))
        else:
            raise ValueError('Need either "engine" or "url" defined')

        SessionCls.configure(bind=self.engine)

    def setup(self) -> None:
        super().setup()
        Base.metadata.create_all(self.engine)

    def teardown(self) -> None:
        super().teardown()
        self.engine.dispose()

    @db_user
    def add_job(self, job: Job, replace_existing: bool = True, session: Optional[Session] = None) -> None:
        """Adds a `Job` to store and track.

        Args:
            job (Job): A 'Job' to store and track.
            replace_existing (bool, optional): Determines if a `Job` matching the one provided
                should be replaced. Defaults to True.
            session (Session, optional): The SQLAlchemy Session to use. Defaults to None.

        Raises:
            JobAlreadyExistsException: If a `Job` matching the one provided is found, but
                `replace_existing` is False.
        """
        if self.contains_job(job.id):
            if not replace_existing:
                raise JobAlreadyExistsException(job.id)

            self.update_job(job, session=session)
            return

        if job.next_run_time is None and job.active:
            job.next_run_time = job.trigger.get_next_fire_time(None, None)

        self._logger.debug(f'Add job ({job}) next run time: {job.next_run_time}')

        next_run_time = cast(Optional[Decimal], job.get_next_run_time_ts())  # See https://github.com/dropbox/sqlalchemy-stubs/issues/178
        new_job = DbJob(id=job.id,
                        next_run_time=next_run_time,
                        job_state=pickle.dumps(job.__getstate__(), self.pickle_protocol))

        session.add(new_job)  # type: ignore

    @db_user
    def update_job(self, job: Job, session: Optional[Session] = None) -> None:
        """Updates an existing `Job` matching the `job.id` with new data.

        Args:
            job (Job): Find a `Job` matching this `job.id` and replace it with this.
            session (Session, optional): An SQLAchemy Session. Defaults to None.
        """
        existing_job = self._get_db_job(job.id, session)  # type: ignore

        if job.next_run_time is None and job.active:
            if existing_job.next_run_time is None:
                job.next_run_time = job.trigger.get_next_fire_time(None, None)
            else:
                tz = self._scheduler.tz  # type: ignore
                job.next_run_time = datetime.fromtimestamp(float(existing_job.next_run_time), tz=tz)

        self._logger.debug(f'Update job ({job}) next run time: {job.next_run_time}')

        next_run_time = cast(Optional[Decimal], job.get_next_run_time_ts())  # See https://github.com/dropbox/sqlalchemy-stubs/issues/178
        existing_job.next_run_time = next_run_time
        existing_job.job_state = pickle.dumps(job.__getstate__(), self.pickle_protocol)

    @db_user
    def remove_job(self, job_id: str, session: Optional[Session] = None) -> None:
        """Removes a single `Job`.

        Args:
            job_id (str): Used to find the `Job` to remove.
            session (Session, optional): An SQLAlchemy Session. Defaults to None.
        """
        existing_job = self._get_db_job(job_id, session)  # type: ignore
        self._logger.debug(f'Delete job ({self._reconstitute_job(existing_job)})')
        session.delete(existing_job)  # type: ignore

    @db_user
    def remove_all_jobs(self, session: Optional[Session] = None) -> None:
        """Removes all `Job`s.

        Args:
            session (Session, optional): An SQLAlchemy Session. Defaults to None.
        """
        session.query(DbJob).delete()  # type: ignore

    @db_user
    def get_job(self, job_id: str, session: Optional[Session] = None) -> Job:
        """Returns a `Job` matching the `job_id`.

        Args:
            job_id (str): Used to find the `Job` to return.
            session (Session, optional): An SQLAlchemy Session. Defaults to None.

        Returns:
            Job: The `Job` associated with the `job_id`.
        """
        existing_job = self._get_db_job(job_id, session)  # type: ignore
        return self._reconstitute_job(existing_job)

    @db_user
    def get_jobs(self, pattern: str = None, session: Optional[Session] = None) -> list[Job]:
        """Returns a list of `Job`s matching the pattern, or all if no pattern.

        Args:
            pattern (str, optional): A regular expression pattern to match against `Job` ids.
                Defaults to None.
            session (Session, optional): An SQLAlchemy Session. Defaults to None.

        Returns:
            List[Job]: A list of `Job`s matching the pattern, or all if no pattern.
        """
        db_jobs = session.query(DbJob).order_by(DbJob.next_run_time.asc()).all()  # type: ignore

        if pattern is not None:
            compiled_pattern = re.compile(pattern)
            db_jobs = list(filter(lambda db_job: compiled_pattern.fullmatch(db_job.id), db_jobs))

        return list(map(lambda db_job: self._reconstitute_job(db_job), db_jobs))

    @db_user
    def contains_job(self, job_id: str, session: Optional[Session] = None) -> bool:
        """Returns if the `JobStore` currently has a `Job`.

        Args:
            job_id (str): Used to find a `Job`.
            session (Session, optional): An SQLAlchemy Session. Defaults to None.

        Returns:
            bool: True of the `JobStore` currently has a `Job` with the `job_id`, False otherwise.
        """
        try:
            self._get_db_job(job_id, session)  # type: ignore
            return True
        except JobDoesNotExistException:
            return False

    @staticmethod
    def _get_db_job(job_id: str, session: Session) -> DbJob:
        """Returns a `Job` from the database.

        Args:
            job_id (str): Used to find a `Job`.
            session (Session): An SQLAlchemy Session.

        Raises:
            JobDoesNotExistException: If the `job_id` does not match any stored `Job`.

        Returns:
            DbJob: A stored, pickled version of the `Job`.
        """
        existing_job = session.query(DbJob).get(job_id)  # type: ignore
        if existing_job is None:
            raise JobDoesNotExistException(job_id)
        return existing_job

    @staticmethod
    def _reconstitute_job(db_job: DbJob) -> Job:
        """Rebuilds a `Job` from a stored `DbJob` entry.

        Args:
            db_job (DbJob): The stored, pickled version of a `Job`.

        Returns:
            Job: A `Job` rebuilt using the data from `DbJob`.
        """
        job_state = pickle.loads(db_job.job_state)
        job = object.__new__(Job)
        job.__setstate__(job_state)
        return job

    @db_user
    def _get_stored_instance_id(self, session: Optional[Session] = None) -> int:
        """Returns the last stored instance id.

        Args:
            session (Session, optional): An SQLAlchemy Session. Defaults to None.

        Returns:
            int: The last stored instance id from the `LastInstanceId` table.
        """
        last_instance_id = session.query(LastInstanceId).get(0)  # type: ignore
        if last_instance_id is None:  # type: ignore
            return 0
        return last_instance_id.id

    @db_user
    def _save_instance_id(self, instance_id: int, session: Optional[Session] = None) -> None:
        """Saves an instance id.

        Args:
            instance_id (int): The instance id to save to the database.
            session (Session, optional): An SQLAlchemy Session. Defaults to None.
        """
        last_instance_id = session.query(LastInstanceId).get(0)  # type: ignore
        if last_instance_id is None:
            last_instance_id = LastInstanceId(row=0, id=instance_id)
            session.add(last_instance_id)  # type: ignore
        else:
            last_instance_id.id = instance_id

        self._logger.debug(f'saved new instance ID ({instance_id})')
