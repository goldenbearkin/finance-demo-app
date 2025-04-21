from app.domain.tickers.schemas import Ticker
import yfinance as yf  # type: ignore
from typing import Any
import pytz
from datetime import datetime, timezone


class TickerService:
    @staticmethod
    def get_ticker_summary(symbol: str) -> Ticker:
        ticker: Any = yf.Ticker(symbol)
        name = ticker.info["longName"]
        symbol = ticker.info["symbol"]

        regular_market_price = ticker.info.get("regularMarketPrice")
        regular_market_price_change = ticker.info.get("regularMarketChange")
        regular_market_percent_change = ticker.info.get("regularMarketChangePercent")
        regular_market_timestamp = ticker.info.get("regularMarketTime")
        regular_market_utc = datetime.fromtimestamp(regular_market_timestamp, tz=timezone.utc)
        regular_market_edt = regular_market_utc.astimezone(pytz.timezone("America/New_York"))
        regular_market_formatted_datetime = regular_market_edt.strftime("%B %-d at %-I:%M:%S %p EDT")

        return Ticker(
            symbol=symbol,
            name=name,
            regularMarketPrice=f"{regular_market_price:.2f}",
            regularMarketPriceChange=f"{regular_market_price_change:.2f}",
            regularMarketPercentChange=f"{regular_market_percent_change:.2f}%",
            regularMarketPriceAt=f"{regular_market_formatted_datetime}",
        )
