import logging
from typing import List

from fastapi import APIRouter, Depends

from fc_auditlog.auditlog import AuditLog
from fc_auditlog.auditlogs import AuditLogAction, AuditLogModule, AuditLogObjectType
from fc_permissions.fc_permissions_deps import HasPermission

from application.config.app_settings import app_settings
from domain_one.api.schemas.user import CreateUserRequest, UpdateUserRequest, UserDetailResponse, UserResponse
from domain_one.core.dtos.user import UserDTO
from domain_one.core.use_cases.users.create_user import CreateUserUseCase
from domain_one.core.use_cases.users.delete_user import DeleteUserUseCase
from domain_one.core.use_cases.users.get_user import GetUserUseCase
from domain_one.core.use_cases.users.get_users import GetUsersUseCase
from domain_one.core.use_cases.users.update_user import UpdateUserUseCase
from domain_one.di import DomainOneContainer


logger = logging.getLogger(app_settings.APP_LOGGER)

router = APIRouter()


def get_users_use_case() -> GetUsersUseCase:
    return DomainOneContainer().get_users_use_case


def get_user_use_case() -> GetUserUseCase:
    return DomainOneContainer().get_user_use_case


def create_user_use_case() -> CreateUserUseCase:
    return DomainOneContainer().create_user_use_case


def update_user_use_case() -> UpdateUserUseCase:
    return DomainOneContainer().update_user_use_case


def delete_user_use_case() -> DeleteUserUseCase:
    return DomainOneContainer().delete_user_use_case


@router.get(
    '/user/',
    tags=['Domain One'],
)
def get_users(
    get_users_use_case: GetUsersUseCase = Depends(get_users_use_case),
    user: str = Depends(HasPermission('user.user_management')),
) -> List[UserResponse]:
    users: list[UserDTO] = get_users_use_case.get_users()
    AuditLog().add_data(
        # In this case we use the user email, but if the action is performed to a specific object, we should use the
        # object uuid
        primary_object_uuid=user,
        primary_object_type=AuditLogObjectType.USER,
        user=user,
        text='Getting all users',
        module=AuditLogModule.DATA_SERVICE,  # Must be changed with the module name
        action=AuditLogAction.RETRIEVED,
    )
    AuditLog().save_audit_log()
    return users


@router.get(
    '/user/{user_id}',
    tags=['Domain One'],
)
def get_user(
    user_id: int,
    get_user_use_case: GetUserUseCase = Depends(get_user_use_case),
    user: str = Depends(HasPermission('user.user_management')),
) -> UserDetailResponse:
    user: UserDTO = get_user_use_case.get_user(user_id)
    AuditLog().add_data(
        primary_object_uuid=user_id,
        primary_object_type=AuditLogObjectType.USER,
        user=user,
        text='Getting user details',
        module=AuditLogModule.DATA_SERVICE,  # Must be changed with the module name
        action=AuditLogAction.RETRIEVED,
    )
    AuditLog().save_audit_log()
    return UserDetailResponse.parse_obj(user)


@router.post(
    '/user/',
    tags=['Domain One'],
)
def create_user(
    request: CreateUserRequest,
    create_user_use_case: CreateUserUseCase = Depends(create_user_use_case),
    user: str = Depends(HasPermission('user.user_management')),
) -> UserDetailResponse:
    user_dto: UserDTO = UserDTO(**request.dict())
    user: UserDTO = create_user_use_case.create_user(user_dto)
    AuditLog().add_data(
        primary_object_uuid=user.id,
        primary_object_type=AuditLogObjectType.USER,
        user=user,
        text='Creating user',
        module=AuditLogModule.DATA_SERVICE,  # Must be changed with the module name
        action=AuditLogAction.RETRIEVED,
    )
    AuditLog().save_audit_log()
    return UserDetailResponse.parse_obj(user)


@router.put(
    '/user/{user_id}',
    tags=['Domain One'],
)
def update_user(
    user_id: int,
    request: UpdateUserRequest,
    update_user_use_case: UpdateUserUseCase = Depends(update_user_use_case),
    user: str = Depends(HasPermission('user.user_management')),
) -> UserDetailResponse:
    user_dto: UserDTO = UserDTO(**request.dict(), id=user_id)
    user: UserDTO = update_user_use_case.update_user(user_dto)
    AuditLog().add_data(
        primary_object_uuid=user_id,
        primary_object_type=AuditLogObjectType.USER,
        user=user,
        text='Updating user, check extra_payload for the changes',
        extra_payload=user_dto.dict(),
        module=AuditLogModule.DATA_SERVICE,  # Must be changed with the module name
        action=AuditLogAction.RETRIEVED,
    )
    AuditLog().save_audit_log()
    return UserDetailResponse.parse_obj(user)


@router.delete(
    '/user/{user_id}',
    tags=['Domain One'],
)
def delete_user(
    user_id: int,
    delete_user_use_case: DeleteUserUseCase = Depends(delete_user_use_case),
    user: str = Depends(HasPermission('user.user_management')),
) -> bool:
    success: bool = delete_user_use_case.delete_user(user_id)
    AuditLog().add_data(
        primary_object_uuid=user_id,
        primary_object_type=AuditLogObjectType.USER,
        user=user,
        text='Deleting user',
        module=AuditLogModule.DATA_SERVICE,  # Must be changed with the module name
        action=AuditLogAction.RETRIEVED,
    )
    AuditLog().save_audit_log()
    return success
