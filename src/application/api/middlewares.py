from datetime import datetime
import logging

from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

from application.config.app_settings import app_settings


logger = logging.getLogger(app_settings.APP_LOGGER)


async def handle_jwt(auth: HTTPAuthorizationCredentials = Security(HTTPBearer())) -> dict:
    token = auth.credentials
    try:
        payload = jwt.decode(token, app_settings.APP_SECRET_KEY, algorithms=['HS256'])
        remaining = datetime.utcfromtimestamp(payload["exp"]) - datetime.utcnow()
        days = remaining.days
        hours = remaining.seconds // 3600
        mins = (remaining.seconds % 3600) // 60
        logger.info(f"Token decoded OK! {days} days, {hours} hours and {mins} minutes until it expires.")
        del payload["exp"]
        del payload["iat"]
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Signature has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')
