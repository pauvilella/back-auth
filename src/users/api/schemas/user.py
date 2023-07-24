from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserSignupRequest(UserBase):
    password: str


class UserSignupResponse(UserBase):
    is_active: bool


# class UserDetailResponse(BaseModel):
#     id: int
#     name: str
#     email: str


# class CreateUserRequest(BaseModel):
#     id: int
#     username: str
#     name: str
#     last_name: str
#     email: str
#     password: str


# class UpdateUserRequest(BaseModel):
#     name: str
#     password: str
