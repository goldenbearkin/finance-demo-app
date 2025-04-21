import { DataGrid } from "@mui/x-data-grid";
import { useFetchPublicEstimation } from "../hooks";
import { TableSkeleton, Subtitle } from "../components";
import { FC } from "react";
import { Box, Stack, SxProps } from "@mui/material";
import { EstimateType } from "../models";

interface PublicEstimationProps {
  type: EstimateType;
  symbol: string;
  sx?: SxProps;
}

export const PublicEstimation: FC<PublicEstimationProps> = ({ type, symbol, sx }) => {
  const { data, isPending } = useFetchPublicEstimation(type, symbol);

  if (isPending || data === undefined)
    return (
      <Box sx={sx}>
        <TableSkeleton />
      </Box>
    );

  const columns = data.columns.map((column) => ({
    ...column,
    flex: 1,
  }));

  return (
    <Stack sx={sx} direction="column" spacing={2}>
      <Subtitle>{data.title}</Subtitle>
      <DataGrid density="compact" disableColumnSorting hideFooter rows={data.rows} columns={columns} />
    </Stack>
  );
};
