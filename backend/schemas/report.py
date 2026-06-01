from pydantic import BaseModel
from datetime import datetime
from typing import Any


class ReportBase(BaseModel):
    user_id: int
    report_json: dict


class ReportResponse(BaseModel):
    id: int
    user_id: int

    report_json: dict

    generated_at: datetime