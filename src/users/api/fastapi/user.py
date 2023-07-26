import logging

from application.api.middlewares import handle_jwt
from application.config.app_settings import app_settings
import bcrypt
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from fastapi.security import HTTPAuthorizationCredentials

from users.api.schemas.user import (
    UserLoginRequest,
    UserLoginResponse,
    UserMeResponse,
    UserSignupRequest,
    UserSignupResponse,
    UserTokenRefreshRequest,
)
from users.core.dtos.user import UserDTO
from users.core.use_cases.users.login_user import LoginUserUseCase, create_jwt_tokens
from users.core.use_cases.users.signup_user import SignupUserUseCase


logger = logging.getLogger(app_settings.APP_LOGGER)

router = APIRouter(prefix="/users")


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


@router.post(
    '/login/',
    tags=['Users'],
)
def login(payload: UserLoginRequest) -> UserLoginResponse:
    tokens = LoginUserUseCase().login_user(payload)
    if not tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return UserLoginResponse(**tokens)


@router.post(
    '/token/refresh/',
    tags=['Users'],
)
async def refresh_tokens(payload: UserTokenRefreshRequest) -> UserLoginResponse:
    data = await handle_jwt(HTTPAuthorizationCredentials(scheme="Bearer", credentials=payload.refresh_token))
    logger.info("Refresh token validated OK! Generating a new pair of tokens.")
    tokens = create_jwt_tokens(data)
    return UserLoginResponse(**tokens)


@router.get(
    '/me/',
    tags=['Users'],
)
def me(data_from_jwt: dict = Depends(handle_jwt)) -> UserMeResponse:
    return UserMeResponse(
        id=data_from_jwt["user_id"],
        email=data_from_jwt["user_email"],
        first_name=data_from_jwt["user_first_name"],
        last_name=data_from_jwt["user_last_name"],
        is_active=data_from_jwt["user_is_active"],
    )
