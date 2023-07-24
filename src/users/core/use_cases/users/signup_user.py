import logging

from application.config.app_settings import app_settings
from users.adapters.user_postgres_repository import UsersPostgresRepository
from users.core.dtos.user import UserDTO


logger = logging.getLogger(app_settings.APP_LOGGER)


class SignupUserUseCase:
    def __init__(self):
        self.user_port = UsersPostgresRepository()

    def signup_user(self, user_dto: UserDTO) -> UserDTO:
        return self.user_port.create_user(user_dto)
