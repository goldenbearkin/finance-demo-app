import { Card, Skeleton, SxProps } from "@mui/material";
import { useFetchChart } from "../hooks";
import HighchartsReact from "highcharts-react-official";
import Highcharts from "highcharts";

interface RevenueVsEarningsChartProps {
  sx?: SxProps;
  symbol: string;
}

export const RevenueVsEarningsChart = ({ symbol, sx }: RevenueVsEarningsChartProps) => {
  const { data: options, isPending, error } = useFetchChart(symbol, "revenue-vs-earnings");

  if (isPending) return <Skeleton sx={{ ...sx }} variant="rectangular" />;

  if (error) return <div>Error: {error.message}</div>;

  return (
    <Card sx={sx}>
      <HighchartsReact highcharts={Highcharts} options={options} />
    </Card>
  );
};
