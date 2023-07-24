from contextlib import AbstractContextManager, contextmanager
import logging
from typing import Callable

from application.config.app_settings import app_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker


logger = logging.getLogger(app_settings.APP_LOGGER)


# Create database engine
engine = create_engine(app_settings.DATABASE_URL, echo=False, future=True)

# Create database declarative base
Base = declarative_base()

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db() -> Callable[..., AbstractContextManager[Session]]:
    session = SessionLocal()
    try:
        yield session
    except Exception:
        logger.exception("Session rollback because of exception", exc_info=True, stack_info=True)
        session.rollback()
        raise
    finally:
        session.close()
