import os

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

    DATABASE_URL = 'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}'.format(
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT'),
        db_name=os.getenv('POSTGRES_DB'),
        username=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
    )

    APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')
    ALGORITHM = 'HS256'

    class Config(object):
        case_sensitive = True


app_settings = AppSettings()
