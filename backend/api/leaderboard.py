from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from services.leaderboard_service import LeaderboardService

router = APIRouter(
    prefix="/leaderboard",
    tags=["Leaderboard"]
)


@router.get("/")
async def get_leaderboard(
    limit: int = 50,
    db: Session = Depends(get_db)
):

    data = LeaderboardService.get_leaderboard(
        db=db,
        limit=limit
    )

    return {
        "leaderboard": [
            {
                "handle": row.handle,
                "search_count": row.total_searches
            }
            for row in data
        ]
    }