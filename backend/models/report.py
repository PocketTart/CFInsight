from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import JSON

from core.database import Base


class Report(Base):

    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    report_json = Column(JSON)

    generated_at = Column(
        DateTime,
        default=datetime.now
    )