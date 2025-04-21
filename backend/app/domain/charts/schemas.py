from pydantic import BaseModel
from typing import Literal, List, Optional


class CssOptions(BaseModel):
    color: str


class YAxisStackLabelsOptions(BaseModel):
    enabled: bool


class ChartOptions(BaseModel):
    type: str
    height: int
    backgroundColor: str


class TitleOptions(BaseModel):
    text: str
    align: Optional[Literal["left", "center", "right"]] = None
    verticalAlign: Optional[Literal["top", "middle", "bottom"]] = None
    style: Optional[CssOptions] = None


class LabelsOptions(BaseModel):
    style: Optional[CssOptions] = None


class AxisCommon(BaseModel):
    title: Optional[TitleOptions] = None
    labels: Optional[LabelsOptions] = None
    lineWidth: Optional[int] = 0
    categories: Optional[List[str]] = None
    min: Optional[int] = 0
    max: Optional[int] = None
    allowDecimals: Optional[bool] = False


class XAxisOptions(AxisCommon):
    pass


class YAxisOptions(AxisCommon):
    visible: Optional[bool] = False
    stackLabels: Optional[YAxisStackLabelsOptions] = None
    gridLineDashStyle: Optional[str] = None
    gridLineColor: Optional[str] = None


class ItemStyleOptions(BaseModel):
    color: str


class LegendOptions(BaseModel):
    layout: Literal["horizontal", "vertical"]
    align: Literal["left", "center", "right"]
    x: Optional[int] = None
    y: Optional[int] = None
    verticalAlign: Literal["top", "middle", "bottom"]
    floating: Optional[bool] = False
    borderWidth: Optional[int] = None
    borderColor: Optional[str] = None
    shadow: Optional[bool] = None
    itemStyle: Optional[ItemStyleOptions] = None


class Tooltip(BaseModel):
    enabled: bool


class PlotColumnDataLabelsOptions(BaseModel):
    enabled: bool


class PlotColumnOptions(BaseModel):
    stacking: Optional[Literal["normal", "overlap", "percent", "stream"]]
    dataLabels: Optional[PlotColumnDataLabelsOptions] = None
    pointWidth: Optional[int] = None


class PlotOptions(BaseModel):
    column: PlotColumnOptions


class SeriesOptionsType(BaseModel):
    type: Literal["column", "line"]
    name: str
    data: List[int]
    stack: Optional[str] = None
    color: str
    borderWidth: Optional[int] = 0


class StackedAndGroupedColumnChartOptions(BaseModel):
    chart: ChartOptions
    title: TitleOptions
    xAxis: XAxisOptions
    yAxis: YAxisOptions
    legend: LegendOptions
    tooltip: Tooltip
    plotOptions: PlotOptions
    series: List[SeriesOptionsType]
