import MuiAppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import { FC, PropsWithChildren } from "react";
import { UserProfile } from "./UserProfile";

export const AppBar: FC<PropsWithChildren> = ({ children }) => {
  return (
    <MuiAppBar position="sticky">
      <Toolbar>
        <Typography variant="h6" noWrap component="div" sx={{ display: { xs: "none", sm: "block" } }}>
          AM Squared
        </Typography>
        {children}
        <Box sx={{ flexGrow: 1 }} />
        <UserProfile />
      </Toolbar>
    </MuiAppBar>
  );
};
