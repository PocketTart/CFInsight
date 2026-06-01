from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from core.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True
    )

    handle = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    current_rating = Column(Integer)

    max_rating = Column(Integer)

    current_rank = Column(String)

    max_rank = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    last_updated = Column(
        DateTime,
        default=datetime.utcnow
    )