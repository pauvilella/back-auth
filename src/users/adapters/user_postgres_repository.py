import datetime
import logging

from application.config.app_settings import app_settings
from infra.databases.postgres import PostgresDatabaseConnection
from sqlalchemy import Column, Date, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from users.core.dtos.user import UserDTO
from users.core.ports.user import UserPort


logger = logging.getLogger(app_settings.APP_LOGGER)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(Date, default=datetime.datetime.utcnow)

    def to_dto(self) -> UserDTO:
        return UserDTO(
            id=self.id,
            name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            password=self.password,
        )

    def update_from_dto(self, user: UserDTO):
        if user.name:
            self.first_name = user.name
        if user.last_name:
            self.last_name = user.last_name
        if user.email:
            self.email = user.email
        if user.password:
            self.password = user.password

    @staticmethod
    def from_dto(user: UserDTO):
        return User(
            id=user.id,
            first_name=user.name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )


class UsersPostgresRepository(UserPort):
    def __init__(self, postgres_connection: PostgresDatabaseConnection):
        self.postgres_connection = postgres_connection

    def get_users(self) -> list[UserDTO]:
        try:
            logger.info("Getting users from PostgreSQL")
            with self.postgres_connection.session() as session:
                users = session.query(User).all()
                users = [user.to_dto() for user in users]
                logger.debug(users)
                return users
        except Exception:
            logger.exception("Getting users from PostgreSQL error")

    def get_user(self, user_id: int) -> UserDTO:
        try:
            logger.info("Getting user from PostgreSQL")
            with self.postgres_connection.session() as session:
                user = session.query(User).filter_by(id=user_id).first().to_dto()
                logger.debug(user)
                return user
        except Exception:
            logger.exception("Getting user from PostgreSQL error")

    def create_user(self, user_dto: UserDTO) -> UserDTO:
        try:
            logger.info("Creating user in PostgreSQL")
            with self.postgres_connection.session() as session:
                user = User().from_dto(user_dto)
                session.add(user)
                session.commit()
                # Get the created user
                user = session.query(User).filter_by(id=user_dto.id).first().to_dto()
                logger.debug(user)
                return user
        except Exception:
            logger.exception("Creating user in PostgreSQL error")

    def update_user(self, user_dto: UserDTO) -> UserDTO:
        try:
            logger.info("Updating user in PostgreSQL")
            with self.postgres_connection.session() as session:
                user_id = user_dto.id
                # Update the user
                user = session.query(User).get(user_id)
                user.update_from_dto(user_dto)
                session.commit()
                # Get the updated user
                user = session.query(User).filter_by(id=user_dto.id).first().to_dto()
                return user
        except Exception:
            logger.exception("Updating user in PostgreSQL error")

    def delete_user(self, user_id: int) -> bool:
        try:
            logger.info("Deleting user in PostgreSQL")
            with self.postgres_connection.session() as session:
                user = session.query(User).get(user_id)
                session.delete(user)
                session.commit()
                return True
        except Exception:
            logger.error(
                '''This method is suposed to fail, as we have not defined all relations that
                user has and needs to be deleted'''
            )
            return False
