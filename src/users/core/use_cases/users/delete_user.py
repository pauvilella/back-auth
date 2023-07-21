# import logging

# from application.config.app_settings import app_settings
# from users.core.ports.user import UserPort


# logger = logging.getLogger(app_settings.APP_LOGGER)


# class DeleteUserUseCase:
#     def __init__(self, user_port: UserPort):
#         self.user_port = user_port

#     def delete_user(self, user_id: int) -> bool:
#         return self.user_port.delete_user(user_id)
