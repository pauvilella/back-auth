from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserLoginResponse(BaseModel):
    token: str


class UserSignupRequest(UserBase):
    password: str


class UserSignupResponse(UserBase):
    is_active: bool
