export const fetchClient = async (url: string, options: RequestInit = {}) => {
  const token = localStorage.getItem("token");
  const addToken: HeadersInit = token ? { Authorization: `Bearer ${token}` } : {};

  const headers = {
    ...(options.headers || {}),
    ...addToken,
    "Content-Type": "application/json",
  };

  const response = await fetch(url, {
    ...options,
    headers,
  });

  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }

  return response;
};
