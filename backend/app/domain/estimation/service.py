from app.db import SessionDep
from app.domain.common.schemas import TableData, TableColumn
from fastapi import HTTPException
from pandas import DataFrame
import yfinance as yf  # type: ignore
from app.domain.estimation.models import PrivateEstimates, EstimationType
from app.domain.estimation.schemas import PrivateEstimatesWrite, PublicEstimatesRead, PrivateEstimatesRead
from sqlmodel import select
import json


class EstimationService:
    def __init__(self, session: SessionDep):
        self.session = session

    def get_earnings_estimates(self, ticker: str) -> TableData[PublicEstimatesRead]:
        earnings: DataFrame = yf.Ticker(ticker).earnings_estimate

        if earnings.empty:
            raise HTTPException(status_code=404, detail=f"Ticker {ticker} not found")

        earnings_dict = earnings.to_dict()  # type: ignore

        return TableData(
            title="Earnings Estimates",
            columns=[
                TableColumn(field="metric", headerName="Currency in USD"),
                TableColumn(field="0q", headerName="Current Qtr. (Mar 2025)"),
                TableColumn(field="+1q", headerName="Next Qtr. (Jun 2025)"),
                TableColumn(field="0y", headerName="Current Year (2025)"),
                TableColumn(field="+1y", headerName="Next Year (2026)"),
            ],
            rows=[
                PublicEstimatesRead(metric="No. of Analysts", **earnings_dict["numberOfAnalysts"]),
                PublicEstimatesRead(metric="Avg. Estimate", **earnings_dict["avg"]),
                PublicEstimatesRead(metric="Low Estimate", **earnings_dict["low"]),
                PublicEstimatesRead(metric="High Estimate", **earnings_dict["high"]),
                PublicEstimatesRead(metric="Year Ago EPS", **earnings_dict["yearAgoEps"]),
            ],
        )

    def get_revenue_estimates(self, ticker: str) -> TableData[PublicEstimatesRead]:
        revenue: DataFrame = yf.Ticker(ticker).revenue_estimate

        if revenue.empty:
            raise HTTPException(status_code=404, detail=f"Ticker {ticker} not found")

        revenue_dict = revenue.to_dict()  # type: ignore

        return TableData(
            title="Revenue Estimates",
            columns=[
                TableColumn(field="metric", headerName="Currency in USD"),
                TableColumn(field="0q", headerName="Current Qtr. (Mar 2025)"),
                TableColumn(field="+1q", headerName="Next Qtr. (Jun 2025)"),
                TableColumn(field="0y", headerName="Current Year (2025)"),
                TableColumn(field="+1y", headerName="Next Year (2026)"),
            ],
            rows=[
                PublicEstimatesRead(metric="No. of Analysts", **revenue_dict["numberOfAnalysts"]),
                PublicEstimatesRead(metric="Avg. Estimate", **revenue_dict["avg"]),
                PublicEstimatesRead(metric="Low Estimate", **revenue_dict["low"]),
                PublicEstimatesRead(metric="High Estimate", **revenue_dict["high"]),
                PublicEstimatesRead(metric="Year Ago EPS", **revenue_dict["yearAgoRevenue"]),
            ],
        )

    def save_private_estimation(self, email: str, estimation_create: PrivateEstimatesWrite):
        statement = select(PrivateEstimates).where(
            PrivateEstimates.email == email,
            PrivateEstimates.symbol == estimation_create.symbol,
            PrivateEstimates.estimation_type == estimation_create.estimation_type,
        )
        estimation = self.session.exec(statement).one_or_none()

        if estimation:
            estimation.estimates = estimation_create.estimates

        else:
            estimation = PrivateEstimates(
                email=email,
                symbol=estimation_create.symbol,
                estimation_type=estimation_create.estimation_type,
                estimates=estimation_create.estimates,
            )

        self.session.add(estimation)
        self.session.commit()
        self.session.refresh(estimation)

    def get_private_estimations(self, email: str, symbol: str, estimation_type: EstimationType) -> TableData[PrivateEstimatesRead]:
        statement = select(PrivateEstimates).where(
            PrivateEstimates.email == email,
            PrivateEstimates.symbol == symbol,
            PrivateEstimates.estimation_type == estimation_type,
        )
        sql_result = self.session.exec(statement).first()
        title = "Your estimates"

        columns = [
            TableColumn(field="period", type="number", headerName="Period"),
            TableColumn(field="estimates", type="number", headerName="Your Estimates", editable=True),
        ]

        if sql_result is None:
            return TableData(
                title=title,
                columns=columns,
                rows=[
                    PrivateEstimatesRead(period="Current Qtr."),
                    PrivateEstimatesRead(period="Next Qtr."),
                    PrivateEstimatesRead(period="Current Year"),
                    PrivateEstimatesRead(period="Next Year"),
                ],
            )

        return TableData(
            title=title,
            columns=columns,
            rows=json.loads(sql_result.estimates),
        )
