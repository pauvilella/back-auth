from fastapi.responses import ORJSONResponse as JSONResponse
from fastapi.routing import APIRouter

from infra.aws.secrets_manager import SecretsManager


# from infra.rabbit.rabbit_consumer import RabbitConsumer


router = APIRouter()

secrets_manager = SecretsManager()
# rabbit_consumer = RabbitConsumer(secrets_manager=secrets_manager)


# @router.on_event('startup')
# async def startup_event():
#     rabbit_consumer.start()


# @router.on_event('shutdown')
# async def shutdown_event():
#     rabbit_consumer.stop_consuming()


@router.get(
    '/',
    response_class=JSONResponse,
    status_code=200,
    tags=['Healhtcheck'],
)
async def healthchecker():
    # if not rabbit_consumer.is_healthy():
    #     raise HTTPException(status_code=503, detail="Rabbit consumer is not healthy")
    return {"status": "Service is healthy"}
