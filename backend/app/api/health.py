from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.session import get_db

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("")
async def health_check():
    return {
        "status": "ok"
    }
    
@router.get("/db")
async def database_health(
    db: Session = Depends(get_db)
):
    db.execute(text("SELECT 1"))
    
    return {
        "status": "ok",
        "database": "connected"
    }