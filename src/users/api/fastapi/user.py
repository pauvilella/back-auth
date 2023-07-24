import logging

from application.api.middlewares import handle_jwt
from application.config.app_settings import app_settings
import bcrypt
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends

from users.api.schemas.user import (
    UserLoginRequest,
    UserLoginResponse,
    UserMeResponse,
    UserSignupRequest,
    UserSignupResponse,
)
from users.core.dtos.user import UserDTO
from users.core.use_cases.users.login_user import LoginUserUseCase
from users.core.use_cases.users.signup_user import SignupUserUseCase


logger = logging.getLogger(app_settings.APP_LOGGER)

router = APIRouter(prefix="/users")


@router.post(
    '/login/',
    tags=['Users'],
)
def login(payload: UserLoginRequest) -> UserLoginResponse:
    token = LoginUserUseCase().login_user(payload)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return UserLoginResponse(token=token)


@router.post(
    '/signup/',
    tags=['Users'],
)
def signup(payload: UserSignupRequest) -> UserSignupResponse:
    hashed_password = bcrypt.hashpw(payload.password.encode(), bcrypt.gensalt())
    user_dto = UserDTO(
        email=payload.email,
        hashed_password=hashed_password,
        first_name=payload.first_name,
        last_name=payload.last_name,
        is_active=True,
    )
    user: UserDTO = SignupUserUseCase().signup_user(user_dto)
    return UserSignupResponse.parse_obj(user)


@router.get(
    '/me/',
    tags=['Users'],
)
def me(data_from_jwt: dict = Depends(handle_jwt)) -> UserMeResponse:
    return UserMeResponse(**data_from_jwt)
