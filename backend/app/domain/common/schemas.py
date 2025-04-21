from typing import List, Literal, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

T = TypeVar("T")


class TableColumn(BaseModel):
    field: str
    type: Optional[int | str] = None
    headerName: str
    width: Optional[int] = None
    align: Optional[Literal["right", "left", "center"]] = None
    headerAlign: Optional[Literal["right", "left", "center"]] = None
    editable: Optional[bool] = None


class TableRow(BaseModel):
    id: UUID = Field(default_factory=uuid4)


class TableData(BaseModel, Generic[T]):
    title: str
    columns: List[TableColumn]
    rows: List[T]
