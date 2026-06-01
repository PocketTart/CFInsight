from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint

from core.database import Base


class SearchStats(Base):

    __tablename__ = "search_stats"

    id = Column(Integer, primary_key=True)

    handle = Column(String, nullable=False)

    search_count = Column(Integer, default=1)

    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)

    last_searched_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("handle", "month", "year"),
    )