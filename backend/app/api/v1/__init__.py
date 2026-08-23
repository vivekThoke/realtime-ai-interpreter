from fastapi import APIRouter

from app.api.v1.translation import router as translation_router

router = APIRouter(prefix="/api/v1")

router.include_router(translation_router)