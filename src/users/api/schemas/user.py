from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    name: str


class UserDetailResponse(BaseModel):
    id: int
    name: str
    email: str


class CreateUserRequest(BaseModel):
    id: int
    username: str
    name: str
    last_name: str
    email: str
    password: str


class UpdateUserRequest(BaseModel):
    name: str
    password: str
