// API Configuration
const config = {
  development: {
    apiUrl: "http://localhost:8000",
  },
  production: {
    apiUrl: "http://localhost:8000",
  },
};

// Get current environment
const env = import.meta.env.MODE || "development";

const apiUrl = import.meta.env.VITE_API_URL;

export const API_URL = apiUrl || config[env as keyof typeof config].apiUrl;

export default config;
