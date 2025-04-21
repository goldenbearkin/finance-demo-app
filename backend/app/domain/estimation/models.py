from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field


class EstimationType(str, Enum):
    EARNINGS = "earnings"
    REVENUE = "revenue"


JsonStr = str


class PrivateEstimates(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    symbol: str
    estimation_type: EstimationType
    estimates: JsonStr = Field(default="[]")
