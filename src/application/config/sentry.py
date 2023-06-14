import logging

import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

from application.config.app_settings import app_settings


logger = logging.getLogger(app_settings.APP_LOGGER)


def init_sentry_configuration():
    if app_settings.APP_ENV in ('test', 'sandbox', 'playground', 'demo', 'prod'):
        sentry_sdk.init(
            dsn=app_settings.SENTRY_DSN,
            environment=app_settings.APP_ENV,
            integrations=[
                StarletteIntegration(transaction_style="endpoint"),
                FastApiIntegration(transaction_style="endpoint"),
            ],
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=0.05,
            # If you wish to associate users to errors (assuming you are using
            # django.contrib.auth) you may enable sending PII data.
            send_default_pii=True,
        )
        logger.info('Sentry is enabled')
    else:
        logger.info('Sentry is disabled')
