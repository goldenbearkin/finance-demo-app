import { Box, Button } from "@mui/material";
import { useAuth } from "../contexts/auth";
import IconButton from "@mui/material/IconButton";
import LogoutIcon from "@mui/icons-material/Logout";
import { useNavigate } from "react-router";

export const UserProfile = () => {
  const navigate = useNavigate();
  const { username, logout } = useAuth();

  if (!username) {
    return <Button onClick={() => navigate("/login")}>Login</Button>;
  }

  return (
    <Box display="flex" alignItems="center" gap={2}>
      <div>hello, {username}</div>
      <IconButton onClick={() => logout()} color="primary" aria-label="logout">
        <LogoutIcon />
      </IconButton>
    </Box>
  );
};
