from datetime import datetime

from sqlalchemy.orm import Session

from models.cache_stats import CacheStats


class CacheStatsRepository:

    @staticmethod
    def get_stats(db: Session):

        stats = db.query(CacheStats).first()

        if not stats:
            stats = CacheStats()
            db.add(stats)
            db.commit()
            db.refresh(stats)

        return stats

    @staticmethod
    def increment_hit(db: Session):

        stats = CacheStatsRepository.get_stats(db)

        stats.cache_hits += 1
        stats.last_updated = datetime.utcnow()

        db.commit()

    @staticmethod
    def increment_miss(db: Session):

        stats = CacheStatsRepository.get_stats(db)

        stats.cache_misses += 1
        stats.last_updated = datetime.utcnow()

        db.commit()