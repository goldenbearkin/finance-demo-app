import { useMutation, useQuery } from "@tanstack/react-query";
import {
  fetchPrivateEstimates,
  fetchPublicEstimates,
  updatePrivateEstimates,
  fetchChart,
  fetchTickerSummary,
} from "./api";
import { TickerSummary } from "./models";
import { TableData } from "./models/TableData";
import { HighChartOptions } from "./models/HighChart";

export function useFetchPublicEstimation(estimation_type: string, symbol: string) {
  return useQuery<TableData>({
    queryKey: ["public-estimations", estimation_type, symbol],
    queryFn: () => fetchPublicEstimates(estimation_type, symbol),
    retry: false,
  });
}

export function useFetchPrivateEstimationsQuer(estimation_type: string, symbol: string) {
  return useQuery<TableData>({
    queryKey: ["private-estimations", estimation_type, symbol],
    queryFn: () => fetchPrivateEstimates(estimation_type, symbol),
    retry: false,
  });
}

export function useUpdatePrivateEstimation(estimation_type: string, symbol: string) {
  return useMutation({
    mutationFn: (payload: string) => updatePrivateEstimates(estimation_type, symbol, payload),
  });
}

export function useFetchChart(symbol: string, chart_type: "revenue-vs-earnings" | "analyst-recommendations") {
  return useQuery<HighChartOptions>({
    queryKey: ["chart", symbol, chart_type],
    queryFn: () => fetchChart(symbol, chart_type),
  });
}

export function useFetchTickerSummary(symbol: string) {
  return useQuery<TickerSummary>({
    queryKey: ["ticker-summary", symbol],
    queryFn: () => fetchTickerSummary(symbol),
  });
}
