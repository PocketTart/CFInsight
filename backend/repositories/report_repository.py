from datetime import datetime

from sqlalchemy.orm import Session

from models.report import Report


class ReportRepository:

    @staticmethod
    def get_by_user_id(db: Session, user_id: int):

        return db.query(Report).filter(
            Report.user_id == user_id
        ).first()

    @staticmethod
    def upsert_report(db: Session, user_id: int, report_json: dict):

        existing = db.query(Report).filter(
            Report.user_id == user_id
        ).first()

        if existing:

            existing.report_json = report_json
            existing.generated_at = datetime.utcnow()

        else:

            existing = Report(
                user_id=user_id,
                report_json=report_json,
                generated_at=datetime.utcnow()
            )

            db.add(existing)

        db.commit()
        db.refresh(existing)

        return existing