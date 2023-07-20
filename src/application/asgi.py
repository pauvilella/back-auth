import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users.api.fastapi.user import router as users_router

from application.api.router import router as application_router
from application.config.app_settings import app_settings


logger = logging.getLogger(app_settings.APP_LOGGER)


app = FastAPI(
    title=app_settings.APP_TITLE,
    description=app_settings.APP_DESCRIPTION,
    debug=app_settings.DEBUG,
    docs_url='/api/docs',
    redoc_url='/api/redoc',
    openapi_url='/api/openapi.json',
)

cors_origin_whitelist = list(filter(None, app_settings.CORS_ORIGIN_WHITELIST.split(',')))

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origin_whitelist or ['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(application_router, prefix='/api')
app.include_router(users_router, prefix='/api')
