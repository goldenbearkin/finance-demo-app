import { Card, Skeleton, SxProps } from "@mui/material";
import { useFetchChart } from "../hooks";
import HighchartsReact from "highcharts-react-official";
import Highcharts from "highcharts";

interface AnalystRecommendationsChartProps {
  sx?: SxProps;
  symbol: string;
}

export const AnalystRecommendationsChart = ({ symbol, sx }: AnalystRecommendationsChartProps) => {
  const { data: options, isPending, error } = useFetchChart(symbol, "analyst-recommendations");

  if (isPending) return <Skeleton sx={{ ...sx }} variant="rectangular" />;

  if (error) return <div>Error: {error.message}</div>;

  return (
    <Card sx={sx}>
      <HighchartsReact highcharts={Highcharts} options={options} />
    </Card>
  );
};
