import {
  Table as MuiTable,
  TableHead as MuiTableHead,
  TableRow as MuiTableRow,
  TableCell as MuiTableCell,
  TableContainer,
  TableBody,
  Paper,
  Stack,
} from "@mui/material";
import { FC } from "react";
import { Subtitle } from "./Subtitle";

interface TableProps {
  title: string;
  headers: string[];
  rows: string[][];
}

export const Table: FC<TableProps> = ({ title, headers, rows }) => {
  return (
    <Stack direction="column">
      <Subtitle>{title}</Subtitle>
      <TableContainer component={Paper}>
        <MuiTable size="small">
          <MuiTableHead>
            <MuiTableRow>
              {headers.map((header) => (
                <MuiTableCell align="right" key={header}>
                  {header}
                </MuiTableCell>
              ))}
            </MuiTableRow>
          </MuiTableHead>
          <TableBody>
            {rows.map((row, rowIndex) => (
              <MuiTableRow key={`${title}-${rowIndex}`}>
                {row.map((cell, cellIndex) => (
                  <MuiTableCell key={`${title}-${rowIndex}-${cellIndex}`} align="right">
                    {cell}
                  </MuiTableCell>
                ))}
              </MuiTableRow>
            ))}
          </TableBody>
        </MuiTable>
      </TableContainer>
    </Stack>
  );
};
