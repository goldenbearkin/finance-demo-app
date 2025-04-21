import { useContext } from "react";
import { AuthContext, IAuthContext } from "./AuthContext";

export const useAuth = (): IAuthContext => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within a AuthProvider");
  }
  return context;
};
