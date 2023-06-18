from pydantic import BaseSettings


class AppSettings(BaseSettings):
    DEBUG: bool = False

    APP_ENV = 'dev'
    APP_TITLE = 'back-auth'
    APP_DESCRIPTION = 'Backend service with authentication'
    CORS_ORIGIN_WHITELIST = ','.join(
        [
            'http://localhost:8000',
        ],
    )

    APP_LOGGER = 'back-auth'

    class Config(object):
        case_sensitive = True

app_settings = AppSettings()
