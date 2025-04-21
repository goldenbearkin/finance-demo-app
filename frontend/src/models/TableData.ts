import { GridRowsProp } from "@mui/x-data-grid";
import { GridColDef } from "@mui/x-data-grid";

export interface TableData {
  title: string;
  columns: GridColDef[];
  rows: GridRowsProp;
}
