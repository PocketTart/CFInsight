from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from models.search_stats import SearchStats


class LeaderboardService:

    @staticmethod
    def get_leaderboard(db: Session, limit: int = 50):

        result = (
            db.query(
                SearchStats.handle,
                func.sum(SearchStats.search_count).label("total_searches")
            )
            .group_by(SearchStats.handle)
            .order_by(desc("total_searches"))
            .limit(limit)
            .all()
        )

        return result