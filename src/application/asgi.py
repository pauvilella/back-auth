import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from fc_auditlog.auditlog_middleware import AuditLogMiddleware

from application.api.router import router as application_router
from application.config.app_settings import app_settings
from application.config.sentry import init_sentry_configuration
from domain_one.api.router import router as domain_one_router


logger = logging.getLogger(app_settings.APP_LOGGER)


app = FastAPI(
    title=app_settings.APP_TITLE,
    description=app_settings.APP_DESCRIPTION,
    debug=app_settings.DEBUG,
    docs_url='/base/docs',
    redoc_url='/base/redoc',
    openapi_url='/base/openapi.json',
)

cors_origin_whitelist = list(filter(None, app_settings.CORS_ORIGIN_WHITELIST.split(',')))

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origin_whitelist or ['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.add_middleware(AuditLogMiddleware)
app.add_middleware(GZipMiddleware)

app.include_router(application_router, prefix='/base')
app.include_router(domain_one_router, prefix='/base')

init_sentry_configuration()
