import { Typography } from "@mui/material";

export const Subtitle = ({ children }: { children: React.ReactNode }) => {
  return (
    <Typography variant="subtitle1" fontWeight="bold">
      {children}
    </Typography>
  );
};
