import logging

from application.config.app_settings import app_settings
import bcrypt
from fastapi import APIRouter

from users.api.schemas.user import UserSignupRequest, UserSignupResponse
from users.core.dtos.user import UserDTO
from users.core.use_cases.users.signup_user import SignupUserUseCase


logger = logging.getLogger(app_settings.APP_LOGGER)

router = APIRouter(prefix="/users")


@router.post(
    '/login/',
    tags=['Users'],
)
def login() -> str:
    return "This is a fake token"


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


# @router.get(
#     '/user/',
#     tags=['Users'],
# )
# def get_users(get_users_use_case: GetUsersUseCase = Depends(get_users_use_case)) -> List[UserResponse]:
#     users: list[UserDTO] = get_users_use_case.get_users()
#     return users


# @router.get(
#     '/user/{user_id}',
#     tags=['Users'],
# )
# def get_user(
#     user_id: int,
#     get_user_use_case: GetUserUseCase = Depends(get_user_use_case),
# ) -> UserDetailResponse:
#     user: UserDTO = get_user_use_case.get_user(user_id)
#     return UserDetailResponse.parse_obj(user)


# @router.post(
#     '/user/',
#     tags=['Users'],
# )
# def create_user(
#     request: CreateUserRequest, create_user_use_case: CreateUserUseCase = Depends(create_user_use_case)
# ) -> UserDetailResponse:
#     user_dto: UserDTO = UserDTO(**request.dict())
#     user: UserDTO = create_user_use_case.create_user(user_dto)
#     return UserDetailResponse.parse_obj(user)


# @router.put(
#     '/user/{user_id}',
#     tags=['Users'],
# )
# def update_user(
#     user_id: int, request: UpdateUserRequest, update_user_use_case: UpdateUserUseCase = Depends(update_user_use_case)
# ) -> UserDetailResponse:
#     user_dto: UserDTO = UserDTO(**request.dict(), id=user_id)
#     user: UserDTO = update_user_use_case.update_user(user_dto)
#     return UserDetailResponse.parse_obj(user)


# @router.delete(
#     '/user/{user_id}',
#     tags=['Users'],
# )
# def delete_user(user_id: int, delete_user_use_case: DeleteUserUseCase = Depends(delete_user_use_case)) -> bool:
#     success: bool = delete_user_use_case.delete_user(user_id)
#     return success
