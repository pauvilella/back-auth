from abc import ABC, abstractclassmethod

from domain_one.core.dtos.user import UserDTO


class UserPort(ABC):
    @abstractclassmethod
    def get_users(self) -> list[UserDTO]:
        pass
