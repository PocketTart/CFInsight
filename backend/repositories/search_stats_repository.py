from datetime import datetime
from sqlalchemy.orm import Session

from models.search_stats import SearchStats
from sqlalchemy import func


class SearchStatsRepository:

    @staticmethod
    def increment_search(db: Session, handle: str):

        now = datetime.utcnow()
        month = now.month
        year = now.year

        record = db.query(SearchStats).filter_by(
            handle=handle,
            month=month,
            year=year
        ).first()

        if record:
            record.search_count += 1
            record.last_searched_at = now
        else:
            record = SearchStats(
                handle=handle,
                month=month,
                year=year,
                search_count=1,
                last_searched_at=now
            )
            db.add(record)

        db.commit()
        db.refresh(record)

        return record
    

    @staticmethod
    def get_handle_frequencies(db):

        return (
            db.query(
                SearchStats.handle,
                func.sum(
                    SearchStats.search_count
                ).label("total")
            )
            .group_by(SearchStats.handle)
            .all()
        )