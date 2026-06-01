from pydantic import BaseModel
from datetime import datetime


class SearchStatsBase(BaseModel):
    handle: str
    month: int
    year: int


class SearchStatsResponse(BaseModel):
    handle: str
    search_count: int
    month: int
    year: int
    last_searched_at: datetime