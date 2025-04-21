import { FC } from "react";
import { EditableTable } from "../components/EditableTable";
import { useFetchPrivateEstimationsQuer, useUpdatePrivateEstimation } from "../hooks";
import { EstimateType } from "../models";
import { SxProps } from "@mui/material";
import TableSkeleton from "../components/TableSkeleton";

interface PrivateEstimationProps {
  type: EstimateType;
  symbol: string;
  sx?: SxProps;
}

export const PrivateEstimation: FC<PrivateEstimationProps> = ({ sx, type, symbol }) => {
  const { data, isPending } = useFetchPrivateEstimationsQuer(type, symbol);
  const { mutate } = useUpdatePrivateEstimation(type, symbol);

  if (isPending || data === undefined) return <TableSkeleton sx={sx} />;

  return (
    <EditableTable
      sx={sx}
      columns={data?.columns ?? []}
      rows={data?.rows ?? []}
      onChange={(estimates) => mutate(JSON.stringify(estimates))}
    />
  );
};
