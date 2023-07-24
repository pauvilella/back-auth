import logging

from application.config.app_settings import app_settings
import bcrypt
import jwt
from users.adapters.user_postgres_repository import UsersPostgresRepository
from users.api.schemas.user import UserLoginRequest


logger = logging.getLogger(app_settings.APP_LOGGER)


class LoginUserUseCase:
    def __init__(self):
        self.user_port = UsersPostgresRepository()

    def login_user(self, login_info: UserLoginRequest) -> str:
        user = self.user_port.get_user_by_email(login_info.email)
        if user is not None:
            is_validated: bool = bcrypt.checkpw(login_info.password.encode(), user.hashed_password)
            if is_validated:
                return jwt.encode(
                    {
                        "id": user.id,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "is_active": user.is_active,
                    },
                    app_settings.APP_SECRET_KEY,
                )
        return None
