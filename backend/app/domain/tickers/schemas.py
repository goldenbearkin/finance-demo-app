from pydantic import BaseModel


class Ticker(BaseModel):
    symbol: str
    name: str
    regularMarketPrice: str
    regularMarketPriceChange: str
    regularMarketPercentChange: str
    regularMarketPriceAt: str
