from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.database import get_db

from services.cache_stats_service import CacheStatsService

router = APIRouter(
    prefix="/cache-stats",
    tags=["Cache Stats"]
)


@router.get("/")
async def get_cache_stats(
    db: Session = Depends(get_db)
):
    return CacheStatsService.get_stats(db)