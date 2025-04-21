import { Typography } from "@mui/material";
import { Stack } from "@mui/material";

interface TickerProps {
  price: string;
  priceChange: string;
  percentageChange: string;
  priceAt: string;
  priceAtType: "At close" | "After hours";
}

export const Ticker = ({ price, priceChange, percentageChange, priceAt, priceAtType }: TickerProps) => {
  const isUp = parseFloat(priceChange) >= 0;
  const prefix = isUp ? "+" : "";

  return (
    <Stack direction="column">
      <Stack direction="row" spacing={1} alignItems="center">
        <Typography variant="h4" component="span" fontWeight="bold" lineHeight={1}>
          {price}
        </Typography>
        <Typography variant="h6" component="span" fontWeight="bold" color={isUp ? "success.main" : "error.main"}>
          {`${prefix}${priceChange} (${prefix}${percentageChange})`}
        </Typography>
      </Stack>
      <Typography variant="caption" color="text.secondary">
        {`${priceAtType}: ${priceAt}`}
      </Typography>
    </Stack>
  );
};
