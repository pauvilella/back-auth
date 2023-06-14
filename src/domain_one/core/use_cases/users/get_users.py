import logging

from application.config.app_settings import app_settings
from domain_one.core.dtos.user import UserDTO
from domain_one.core.ports.user import UserPort


logger = logging.getLogger(app_settings.APP_LOGGER)


class GetUsersUseCase:
    def __init__(self, user_port: UserPort):
        self.user_port = user_port

    def get_users(self) -> list[UserDTO]:
        users = self.user_port.get_users()
        return users
