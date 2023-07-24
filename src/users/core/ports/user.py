from abc import ABC, abstractclassmethod

from users.core.dtos.user import UserDTO


class UserPort(ABC):
    @abstractclassmethod
    def create_user(self, user: UserDTO) -> UserDTO:
        ...

    # @abstractclassmethod
    # def get_users(self) -> list[UserDTO]:
    #     ...

    # @abstractclassmethod
    # def get_user(self, user_id: int) -> UserDTO:
    #     ...

    # @abstractclassmethod
    # def update_user(self, user: UserDTO) -> UserDTO:
    #     ...

    # @abstractclassmethod
    # def create_user(self, user: UserDTO) -> UserDTO:
    #     ...

    # @abstractclassmethod
    # def delete_user(self, user_id: int) -> bool:
    ...
