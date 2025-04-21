from app.domain.charts.schemas import (
    StackedAndGroupedColumnChartOptions,
    ChartOptions,
    TitleOptions,
    CssOptions,
    XAxisOptions,
    YAxisOptions,
    LegendOptions,
    Tooltip,
    PlotOptions,
    PlotColumnOptions,
    SeriesOptionsType,
    LabelsOptions,
    ItemStyleOptions,
    YAxisStackLabelsOptions,
    PlotColumnDataLabelsOptions,
)
import yfinance as yf  # type: ignore
from pandas import DataFrame
from typing import Any


class ChartService:
    @staticmethod
    def get_revenue_vs_earnings(ticker: str) -> StackedAndGroupedColumnChartOptions:
        df: DataFrame = yf.Ticker(ticker).quarterly_financials
        df = df.iloc[:, :-1]
        earnings_serie: Any = df.loc["Net Income"]
        revenue_serie: Any = df.loc["Total Revenue"]

        return StackedAndGroupedColumnChartOptions(
            chart=ChartOptions(
                type="column",
                height=270,
                backgroundColor="#1c2228",
            ),
            title=TitleOptions(
                text="Revenue vs Earnings",
                align="left",
                verticalAlign="top",
                style=CssOptions(color="#e2e2e2"),
            ),
            xAxis=XAxisOptions(
                labels=LabelsOptions(style=CssOptions(color="#e2e2e2")),
                categories=["Q1'24", "Q2'24", "Q3'24", "Q4'24"],
            ),
            yAxis=YAxisOptions(
                title=TitleOptions(text=""),
                labels=LabelsOptions(style=CssOptions(color="#e2e2e2")),
                gridLineColor="#363f44",
                gridLineDashStyle="Dash",
            ),
            legend=LegendOptions(
                layout="horizontal",
                align="center",
                verticalAlign="top",
                itemStyle=ItemStyleOptions(color="#e2e2e2"),
            ),
            tooltip=Tooltip(enabled=False),
            plotOptions=PlotOptions(column=PlotColumnOptions(stacking="normal")),
            series=[
                SeriesOptionsType(type="column", name="Revenue", data=revenue_serie.to_list(), stack="Revenue", color="#3a90c8"),
                SeriesOptionsType(type="column", name="Earnings", data=earnings_serie.to_list(), stack="Earnings", color="#f8c268"),
            ],
        )

    @staticmethod
    def analyst_recommendations(ticker: str) -> StackedAndGroupedColumnChartOptions:
        df: Any = yf.Ticker(ticker).recommendations
        df = df.set_index("period")
        strong_buy = df["strongBuy"].to_list()
        buy = df["buy"].to_list()
        hold = df["hold"].to_list()
        sell = df["sell"].to_list()
        strong_sell = df["strongSell"].to_list()

        return StackedAndGroupedColumnChartOptions(
            chart=ChartOptions(
                type="column",
                height=270,
                backgroundColor="#1c2228",
            ),
            title=TitleOptions(
                text="Analyst Recommendations",
                align="left",
                verticalAlign="top",
                style=CssOptions(color="#e2e2e2"),
            ),
            xAxis=XAxisOptions(
                labels=LabelsOptions(style=CssOptions(color="#e2e2e2")),
                categories=["Jan", "Feb", "Mar", "Apr"],
                lineWidth=0,
            ),
            yAxis=YAxisOptions(
                visible=False,
                stackLabels=YAxisStackLabelsOptions(enabled=True),
            ),
            legend=LegendOptions(
                layout="vertical",
                align="right",
                verticalAlign="top",
                borderWidth=0,
                x=-10,
                y=90,
                itemStyle=ItemStyleOptions(color="#e2e2e2"),
            ),
            tooltip=Tooltip(enabled=False),
            plotOptions=PlotOptions(
                column=PlotColumnOptions(
                    stacking="normal",
                    dataLabels=PlotColumnDataLabelsOptions(enabled=True),
                    pointWidth=20,
                ),
            ),
            series=[
                SeriesOptionsType(type="column", name="Strong Buy", data=strong_buy, color="#00aa76"),
                SeriesOptionsType(type="column", name="Buy", data=buy, color="#8ba36b"),
                SeriesOptionsType(type="column", name="Hold", data=hold, color="#bb9f3b"),
                SeriesOptionsType(type="column", name="Underperform", data=sell, color="#dd7849"),
                SeriesOptionsType(type="column", name="Sell", data=strong_sell, color="#ff4143"),
            ],
        )
