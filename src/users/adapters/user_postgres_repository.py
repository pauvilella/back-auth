import logging

from application.config.app_settings import app_settings
from infra.databases.postgres import Base, get_db
from pydantic import EmailStr
from sqlalchemy import Boolean, Column, Integer, LargeBinary, PrimaryKeyConstraint, String, UniqueConstraint
from users.core.dtos.user import UserDTO
from users.core.ports.user import UserPort


logger = logging.getLogger(app_settings.APP_LOGGER)


class User(Base):
    """Models a user table"""

    __tablename__ = "users"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    email = Column(String(225), nullable=False, unique=True)
    hashed_password = Column(LargeBinary, nullable=False)
    first_name = Column(String(225), nullable=False)
    last_name = Column(String(225), nullable=False)
    is_active = Column(Boolean, default=False)

    PrimaryKeyConstraint("id", name="pk_user_id")
    UniqueConstraint("email", name="uq_user_email")

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<User {full_name!r}>".format(full_name=self.first_name + ' ' + self.last_name)

    def to_dto(self) -> UserDTO:
        return UserDTO(
            id=self.id,
            email=self.email,
            hashed_password=self.hashed_password,
            first_name=self.first_name,
            last_name=self.last_name,
            is_active=self.is_active,
        )

    def update_from_dto(self, user: UserDTO):
        if user.email:
            self.email = user.email
        if user.hashed_password:
            self.hashed_password = user.hashed_password
        if user.first_name:
            self.first_name = user.first_name
        if user.last_name:
            self.last_name = user.last_name
        if user.is_active:
            self.is_active = user.is_active

    @staticmethod
    def from_dto(user: UserDTO):
        return User(
            id=user.id,
            email=user.email,
            hashed_password=user.hashed_password,
            first_name=user.first_name,
            last_name=user.last_name,
            is_active=user.is_active,
        )


class UsersPostgresRepository(UserPort):
    def __init__(self):
        ...

    def create_user(self, user: UserDTO) -> UserDTO:
        try:
            logger.info("Creating user in PostgreSQL")
            db_user = User().from_dto(user)
            with get_db() as session:
                session.add(db_user)
                session.commit()
                session.refresh(db_user)
                logger.debug(db_user)
                logger.info("User created successfully!")
                return db_user.to_dto()
        except Exception:
            logger.exception("Error creating user in PostgreSQL")

    def get_user_by_email(self, email: EmailStr) -> UserDTO:
        try:
            logger.info(f"Getting user by email: {email}")
            with get_db() as session:
                user_from_db: User = session.query(User).filter(User.email == email).one()
                if user_from_db:
                    logger.info(f"User found! {user_from_db}")
                    return user_from_db.to_dto()
                else:
                    logger.warning(f"Not found any user with email: {email}")
                    return None
        except Exception:
            logger.exception("Error creating user in PostgreSQL")
