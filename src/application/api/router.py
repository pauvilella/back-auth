from fastapi.responses import ORJSONResponse
from fastapi.routing import APIRouter


router = APIRouter()


@router.get(
    '/',
    response_class=ORJSONResponse,
    status_code=200,
    tags=['Healhtcheck'],
)
async def healthchecker():
    return {"status": "Service is healthy"}
