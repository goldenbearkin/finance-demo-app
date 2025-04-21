import { useState } from "react";
import { Container, Stack } from "@mui/material";
import { AppBar, TickerSearch, Section } from "../components";
import {
  TickerSummary,
  PrivateEstimation,
  PublicEstimation,
  RevenueVsEarningsChart,
  AnalystRecommendationsChart,
} from "../containers";
import { useAuth } from "../contexts/auth";

const chartSx = { width: 350, height: 270 };
const publicTableSx = { flexGrow: 1, minWidth: 0 };
const privateTableSx = { width: 300 };

export const AnalysisPage = () => {
  const { username } = useAuth();
  const [symbol, setSymbol] = useState("MSFT");

  return (
    <div>
      <AppBar>
        <TickerSearch value={symbol} onChange={setSymbol} />
      </AppBar>
      <Container sx={{ paddingTop: 2 }}>
        <Stack direction="column" spacing={2}>
          <TickerSummary symbol={symbol} />
          <Section title="Research Analysis">
            <RevenueVsEarningsChart symbol={symbol} sx={chartSx} />
            <AnalystRecommendationsChart symbol={symbol} sx={chartSx} />
          </Section>
          <Section>
            <PublicEstimation sx={publicTableSx} type="earnings" symbol={symbol} />
            {username && <PrivateEstimation sx={privateTableSx} type="earnings" symbol={symbol} />}
          </Section>
          <Section>
            <PublicEstimation sx={publicTableSx} type="revenue" symbol={symbol} />
            {username && <PrivateEstimation sx={privateTableSx} type="revenue" symbol={symbol} />}
          </Section>
        </Stack>
      </Container>
    </div>
  );
};
