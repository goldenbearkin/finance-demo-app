import { render, screen } from "@testing-library/react";
import { describe, test, expect } from "vitest";
import { http, HttpResponse } from "msw";
import { TickerSummary } from "./TickerSummary";
import { server } from "../mocks/server";
import { createQueryClientWrapper } from "../test-utils";

const Wrapper = createQueryClientWrapper();

describe("TickerSummary", () => {
  test("shows loading state initially", async () => {
    render(<TickerSummary symbol="AAPL" />, { wrapper: Wrapper });
    expect(await screen.findByTestId("skeleton")).toBeInTheDocument();
  });

  test("displays ticker summary data after loading", async () => {
    render(<TickerSummary symbol="AAPL" />, { wrapper: Wrapper });

    expect(await screen.findByText(/AAPL Corporation \(AAPL\)/i)).toBeInTheDocument();

    expect(screen.getByText("150.75")).toBeInTheDocument();
    expect(screen.getByText("+2.50 (+1.68%)")).toBeInTheDocument();
    expect(screen.getByText("At close: April 17 at 4:00:02 PM EDT")).toBeInTheDocument();
  });

  test("shows error state when API call fails", async () => {
    server.use(
      http.get("*/tickers/ERROR", () => {
        return HttpResponse.error();
      })
    );

    render(<TickerSummary symbol="ERROR" />, { wrapper: Wrapper });

    expect(await screen.findByText("error")).toBeInTheDocument();
  });
});
