from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.report import Report


class CacheService:

    TTL_DAYS = 7
    MAX_REPORTS = 1000
    BATCH_DELETE = 50

    @staticmethod
    def is_expired(generated_at: datetime) -> bool:

        if not generated_at:
            return True

        return datetime.utcnow() - generated_at > timedelta(days=CacheService.TTL_DAYS)

    @staticmethod
    def cleanup(db: Session):

        # STEP 1: delete expired reports (>7 days)
        cutoff = datetime.utcnow() - timedelta(days=CacheService.TTL_DAYS)

        db.query(Report).filter(
            Report.generated_at < cutoff
        ).delete(synchronize_session=False)

        db.commit()

        # STEP 2: incremental eviction (only 50 at a time)
        total = db.query(Report).count()

        if total > CacheService.MAX_REPORTS:

            old_reports = db.query(Report).order_by(
                Report.generated_at.asc()
            ).limit(CacheService.BATCH_DELETE).all()

            for r in old_reports:
                db.delete(r)

            db.commit()