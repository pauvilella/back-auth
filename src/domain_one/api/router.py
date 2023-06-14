from fastapi.routing import APIRouter

from domain_one.api.fastapi.user import router as user_router


router = APIRouter(prefix="/domain-one")
router.include_router(user_router)
