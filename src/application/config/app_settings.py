from pydantic import BaseSettings


class AppSettings(BaseSettings):
    DEBUG: bool = False

    APP_ENV = 'dev'
    APP_TITLE = 'Komunica'
    APP_DESCRIPTION = 'Backend service for Komunica'
    CORS_ORIGIN_WHITELIST = ','.join(
        [
            'http://localhost:8000',
        ],
    )

    APP_LOGGER = 'komunica'

    class Config(object):
        case_sensitive = True

app_settings = AppSettings()
