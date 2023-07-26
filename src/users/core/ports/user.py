from abc import ABC, abstractclassmethod

from pydantic import EmailStr
from users.core.dtos.user import UserDTO


class UserPort(ABC):
    @abstractclassmethod
    def create_user(self, user: UserDTO) -> UserDTO:
        ...

    @abstractclassmethod
    def get_user_by_email(self, email: EmailStr) -> UserDTO:
        ...
