from contextlib import AbstractContextManager, contextmanager
import logging
from typing import Callable

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session

from application.config.app_settings import app_settings


logger = logging.getLogger(app_settings.APP_LOGGER)

Base = orm.declarative_base()


class PostgresDatabaseConnection:
    def __init__(self, conn_uri: str) -> None:
        logger.info("Setting up PostgreSQL Database Conneciton")

        self._engine = create_engine(conn_uri, max_overflow=0)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )
        logger.info("PostgreSQL Database Conneciton correctly set up")

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception", exc_info=True, stack_info=True)
            session.rollback()
            raise
        finally:
            session.close()
