from fastapi import APIRouter
from .user import router as users_router

from core.config import settings

router = APIRouter(
    prefix=settings.api_v1.prefix,

)

router.include_router(
    router=users_router,
    prefix=settings.api_v1.users
)