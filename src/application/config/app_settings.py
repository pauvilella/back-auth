from pydantic import BaseSettings


class AppSettings(BaseSettings):
    DEBUG: bool = False

    APP_ENV = 'dev'
    APP_TITLE = 'Fundcraft Base Service'
    APP_DESCRIPTION = 'Fundcraft base service template.'
    CORS_ORIGIN_WHITELIST = ','.join(
        [
            'http://localhost:3000',
            'http://localhost:8080',
        ],
    )

    APP_LOGGER = 'base-service'

    APP_SECRET_MANAGER_NAME = 'base-service-' + APP_ENV

    DATABASE_DRIVER = 'postgresql'
    DATABASE_HOST = 'postgres'
    DATABASE_USER = 'fundcraft'
    DATABASE_NAME = 'fundcraft'
    SECRETS_DATBASE_PASSWORD_KEY = 'database_password'

    SENTRY_DSN = ''

    class Config(object):
        case_sensitive = True


app_settings = AppSettings()
