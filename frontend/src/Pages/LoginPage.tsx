import { Box } from "@mui/material";
import { Card } from "@mui/material";
import { LoginForm } from "../components";

export const LoginPage = () => {
  return (
    <Box display="flex" justifyContent="center" alignItems="center" width="100vw" height="100vh">
      <Card sx={{ padding: 4, width: 400, height: 400 }}>
        <LoginForm />
      </Card>
    </Box>
  );
};
