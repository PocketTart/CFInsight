from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime

from core.database import Base


class CacheStats(Base):

    __tablename__ = "cache_stats"

    id = Column(
        Integer,
        primary_key=True
    )

    cache_hits = Column(
        Integer,
        default=0
    )

    cache_misses = Column(
        Integer,
        default=0
    )

    last_updated = Column(
        DateTime,
        default=datetime.utcnow
    )