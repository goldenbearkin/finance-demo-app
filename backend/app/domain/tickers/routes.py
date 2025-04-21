from fastapi import APIRouter, Depends
from app.domain.tickers.schemas import Ticker
from app.domain.tickers.service import TickerService
from typing import Annotated

router = APIRouter(prefix="/tickers", tags=["tickers"])


@router.get("/{symbol}", response_model=Ticker)
async def get_ticker_summary(symbol: str, ticker_service: Annotated[TickerService, Depends()]):
    return ticker_service.get_ticker_summary(symbol)
