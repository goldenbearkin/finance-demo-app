import { http, HttpResponse, delay } from "msw";
import { TickerSummary } from "../models/TickerSummary";

const TEST_API_URL = "http://localhost:8000";

export const handlers = [
  http.get(`${TEST_API_URL}/tickers/:symbol`, async ({ params }) => {
    const symbol = params.symbol as string;

    const mockTickerSummary: TickerSummary = {
      symbol: symbol,
      name: `${symbol} Corporation`,
      regularMarketPrice: "150.75",
      regularMarketPriceChange: "2.50",
      regularMarketPercentChange: "1.68%",
      regularMarketPriceAt: "April 17 at 4:00:02 PM EDT",
    };
    await delay();
    return HttpResponse.json(mockTickerSummary);
  }),
];
