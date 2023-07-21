import logging

from application.config.app_settings import app_settings
from fastapi import APIRouter


logger = logging.getLogger(app_settings.APP_LOGGER)

router = APIRouter(prefix="/users")


# def get_users_use_case() -> GetUsersUseCase:
#     return GetUsersUseCase(UserPort)


# def get_user_use_case() -> GetUserUseCase:
#     return GetUserUseCase(UserPort)


# def create_user_use_case() -> CreateUserUseCase:
#     return CreateUserUseCase(UserPort)


# def update_user_use_case() -> UpdateUserUseCase:
#     return UpdateUserUseCase(UserPort)


# def delete_user_use_case() -> DeleteUserUseCase:
#     return DeleteUserUseCase(UserPort)


@router.post(
    '/login/',
    tags=['Users'],
)
def login() -> str:
    return "This is a fake token"


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
