import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Skeleton,
  Typography,
  Stack,
  SxProps,
} from "@mui/material";

interface TableSkeletonProps {
  sx?: SxProps;
  rows?: number;
  columns?: number;
}

export const TableSkeleton = ({ sx, rows = 5, columns = 5 }: TableSkeletonProps) => {
  return (
    <Stack direction="column" sx={sx}>
      <Typography variant="h6">
        <Skeleton width="20%" />
      </Typography>
      <TableContainer component={Paper}>
        <Table size="small">
          <TableHead>
            <TableRow>
              {[...Array(columns)].map((_, i) => (
                <TableCell key={i}>
                  <Skeleton width="80%" />
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {[...Array(rows)].map((_, rowIndex) => (
              <TableRow key={rowIndex}>
                {[...Array(columns)].map((_, colIndex) => (
                  <TableCell key={colIndex}>
                    <Skeleton width="100%" />
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Stack>
  );
};

export default TableSkeleton;
