from fastapi import APIRouter, Depends
from redis import Redis
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.db.session import get_db

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
async def health_check():
    return {"status": "ok"}


@router.get("/db")
async def database_health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {"status": "ok", "database": "connected"}


@router.get("/redis")
async def redis_health():
    settings = get_settings()

    client = Redis.from_url(settings.redis_url)

    try:
        client.ping()

        return {"status": "ok", "redis": "connected"}
    finally:
        client.close()
