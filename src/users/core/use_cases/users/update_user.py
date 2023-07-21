# import logging

# from application.config.app_settings import app_settings
# from users.core.dtos.user import UserDTO
# from users.core.ports.user import UserPort


# logger = logging.getLogger(app_settings.APP_LOGGER)


# class UpdateUserUseCase:
#     def __init__(self, user_port: UserPort):
#         self.user_port = user_port

#     def update_user(self, user: UserDTO) -> UserDTO:
#         return self.user_port.update_user(user)
