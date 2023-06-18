from fastapi.responses import ORJSONResponse as JSONResponse
from fastapi.routing import APIRouter


router = APIRouter()

@router.get(
    '/',
    response_class=JSONResponse,
    status_code=200,
    tags=['Healhtcheck'],
)
async def healthchecker():
    return {"status": "Service is healthy"}
