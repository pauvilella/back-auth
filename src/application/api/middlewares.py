from datetime import datetime
import logging

from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

from application.config.app_settings import app_settings


logger = logging.getLogger(app_settings.APP_LOGGER)


def handle_jwt(auth: HTTPAuthorizationCredentials = Security(HTTPBearer())) -> dict:
    token = auth.credentials
    try:
        payload = jwt.decode(token, app_settings.APP_SECRET_KEY, algorithms=['HS256'])
        remaining = datetime.utcfromtimestamp(payload["exp"]) - datetime.utcnow()
        logger.info("Token decoded OK, minutes until expiry %.2f" % (remaining.seconds / 60))
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Signature has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')
