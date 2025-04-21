import { createContext } from "react";

export interface IAuthContext {
  username: string | null;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
}

export const AuthContext = createContext<IAuthContext | undefined>(undefined);
