from fc_common.di.container import DIContainer
from fc_common.di.provider import ProviderFactory
from fc_common.utils.singleton import singleton

from application.config.app_settings import app_settings
from domain_one.adapters.user_postgres_repository import UsersPostgresRepository
from domain_one.core.use_cases.users.create_user import CreateUserUseCase
from domain_one.core.use_cases.users.delete_user import DeleteUserUseCase
from domain_one.core.use_cases.users.get_user import GetUserUseCase
from domain_one.core.use_cases.users.get_users import GetUsersUseCase
from domain_one.core.use_cases.users.update_user import UpdateUserUseCase
from infra.aws.secrets_manager import SecretsManager
from infra.databases.postgres import PostgresDatabaseConnection


@singleton
class DomainOneContainer(DIContainer):
    provider = ProviderFactory()

    @staticmethod
    def setup(provider: ProviderFactory) -> None:
        secrets_manager = SecretsManager()

        database_password = secrets_manager.try_get_secret(
            'base-service-' + app_settings.APP_ENV, app_settings.SECRETS_DATBASE_PASSWORD_KEY
        )

        conn_uri = "{}://{}:{}@{}/{}".format(
            app_settings.DATABASE_DRIVER,
            app_settings.DATABASE_USER,
            database_password,
            app_settings.DATABASE_HOST,
            app_settings.DATABASE_NAME,
        )

        postgres_connection = PostgresDatabaseConnection(conn_uri=conn_uri)

        user_port = provider.register(
            'user_port',
            UsersPostgresRepository,
            postgres_connection=postgres_connection,
        )

        provider.register(
            'get_users_use_case',
            GetUsersUseCase,
            user_port=user_port,
        )

        provider.register(
            'get_user_use_case',
            GetUserUseCase,
            user_port=user_port,
        )

        provider.register(
            'create_user_use_case',
            CreateUserUseCase,
            user_port=user_port,
        )

        provider.register(
            'update_user_use_case',
            UpdateUserUseCase,
            user_port=user_port,
        )

        provider.register(
            'delete_user_use_case',
            DeleteUserUseCase,
            user_port=user_port,
        )
