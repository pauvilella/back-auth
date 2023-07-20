import logging

from application.config.app_settings import app_settings
from users.core.dtos.user import UserDTO
from users.core.ports.user import UserPort


logger = logging.getLogger(app_settings.APP_LOGGER)


class GetUserUseCase:
    def __init__(self, user_port: UserPort):
        self.user_port = user_port

    def get_user(self, user_id: int) -> UserDTO:
        return self.user_port.get_user(user_id)
