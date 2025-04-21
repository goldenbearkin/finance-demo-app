from fastapi import APIRouter
from app.domain.charts.schemas import StackedAndGroupedColumnChartOptions
from app.domain.charts.service import ChartService

router = APIRouter(prefix="/charts", tags=["charts"])


@router.get("/revenue-vs-earnings", response_model=StackedAndGroupedColumnChartOptions, response_model_exclude_none=True)
async def get_revenue_vs_earnings(symbol: str):
    return ChartService.get_revenue_vs_earnings(symbol)


@router.get("/analyst-recommendations", response_model=StackedAndGroupedColumnChartOptions, response_model_exclude_none=True)
async def get_analyst_recommendations(symbol: str):
    return ChartService.analyst_recommendations(symbol)
