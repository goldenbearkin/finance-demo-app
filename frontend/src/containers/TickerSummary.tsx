import { FC } from "react";
import { Box, Typography, Stack, SxProps, Divider, Skeleton } from "@mui/material";
import { Ticker } from "../components/Ticker";
import { useFetchTickerSummary } from "../hooks";

interface TickerSummaryProps {
  sx?: SxProps;
  symbol: string;
}

export const TickerSummary: FC<TickerSummaryProps> = ({ sx, symbol }) => {
  const { data, isPending, error } = useFetchTickerSummary(symbol);

  if (isPending) return <Skeleton data-testid="skeleton" sx={{ ...sx }} variant="rectangular" />;
  if (error) return "error";

  return (
    <Box sx={sx}>
      <Stack spacing={1}>
        <Box>
          <Typography variant="h5" fontWeight="bold">
            {data?.name} ({symbol})
          </Typography>
        </Box>
        <Divider />
        <Stack direction="row" spacing={2}>
          <Ticker
            price={data?.regularMarketPrice}
            priceChange={data?.regularMarketPriceChange}
            percentageChange={data?.regularMarketPercentChange}
            priceAt={data?.regularMarketPriceAt}
            priceAtType="At close"
          />
        </Stack>
      </Stack>
    </Box>
  );
};
