from pydantic import BaseModel, ConfigDict, Field, field_serializer
from typing import Optional
from app.domain.estimation.models import EstimationType
from app.utils.formatting import to_shorter_number
from app.domain.common.schemas import TableRow


class PublicEstimatesRead(TableRow):
    model_config = ConfigDict(validate_by_alias=True)

    metric: str
    curr_month: float = Field(validation_alias="0q", alias="0q")
    next_month: float = Field(validation_alias="+1q", alias="+1q")
    curr_year: float = Field(validation_alias="0y", alias="0y")
    next_year: float = Field(validation_alias="+1y", alias="+1y")

    @field_serializer("curr_month", "next_month", "curr_year", "next_year")
    def serialize_as_str(self, v: float) -> str:
        return to_shorter_number(v)


class PrivateEstimatesRead(TableRow):
    period: str
    estimates: Optional[float] = None


class PrivateEstimatesWrite(BaseModel):
    estimation_type: EstimationType
    symbol: str
    estimates: str
