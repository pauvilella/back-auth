from datetime import datetime, timedelta
import logging

from application.config.app_settings import app_settings
import bcrypt
import jwt
from users.adapters.user_postgres_repository import UsersPostgresRepository
from users.api.schemas.user import UserLoginRequest


logger = logging.getLogger(app_settings.APP_LOGGER)


def create_jwt_tokens(data):
    access_token = jwt.encode(
        {
            **data,
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
        },
        app_settings.APP_SECRET_KEY,
        algorithm="HS256",
    )
    refresh_token = jwt.encode(
        {
            **data,
            'exp': datetime.utcnow() + timedelta(days=7),
            'iat': datetime.utcnow(),
        },
        app_settings.APP_SECRET_KEY,
        algorithm="HS256",
    )
    return {"access_token": access_token, "refresh_token": refresh_token}


class LoginUserUseCase:
    def __init__(self):
        self.user_port = UsersPostgresRepository()

    def login_user(self, login_info: UserLoginRequest) -> str:
        user = self.user_port.get_user_by_email(login_info.email)
        if user is not None:
            is_validated: bool = bcrypt.checkpw(login_info.password.encode(), user.hashed_password)
            if is_validated:
                return create_jwt_tokens(
                    {
                        "user_id": user.id,
                        "user_email": user.email,
                        "user_first_name": user.first_name,
                        "user_last_name": user.last_name,
                        "user_is_active": user.is_active,
                    }
                )
