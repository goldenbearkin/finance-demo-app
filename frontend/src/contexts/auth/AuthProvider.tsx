import { FC, PropsWithChildren, useEffect, useState } from "react";
import { AuthContext } from "./AuthContext";
import { fetchToken, fetchUser } from "../../api";

export const AuthProvider: FC<PropsWithChildren> = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [username, setUsername] = useState(null);

  useEffect(() => {
    if (token) {
      async function getUser() {
        const user = await fetchUser(token as string);
        setUsername(user.username);
      }
      getUser();
    }
  }, [token]);

  const login = async (username: string, password: string) => {
    const response = await fetchToken(username, password);

    if (response?.access_token) {
      setToken(response.access_token);
      localStorage.setItem("token", response.access_token);
      const userProfile = await fetchUser(response.access_token);
      setUsername(userProfile.username);
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUsername(null);
  };

  return <AuthContext.Provider value={{ username, login, logout }}>{children}</AuthContext.Provider>;
};
