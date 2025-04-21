import { API_URL } from "./config";
import { fetchClient } from "./http";

export async function fetchPublicEstimates(estimation_type: string, symbol: string) {
  const res = await fetchClient(`${API_URL}/estimates/public?estimation_type=${estimation_type}&symbol=${symbol}`, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (!res.ok) throw new Error("Network response was not ok");
  return res.json();
}

export async function fetchPrivateEstimates(estimation_type: string, symbol: string) {
  const res = await fetchClient(`${API_URL}/estimates/private?estimation_type=${estimation_type}&symbol=${symbol}`, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (!res.ok) throw new Error("Network response was not ok");
  return res.json();
}

export async function updatePrivateEstimates(estimation_type: string, symbol: string, estimates: string) {
  const res = await fetchClient(`${API_URL}/estimates/private?estimation_type=${estimation_type}&symbol=${symbol}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ estimation_type, symbol, estimates }),
  });
  if (!res.ok) throw new Error("Network response was not ok");
  return res.json();
}

export async function fetchUser(token: string) {
  const res = await fetch(`${API_URL}/users/me/`, {
    method: "GET",
    headers: { Authorization: `Bearer ${token}` },
  });

  if (!res.ok) throw new Error("Network response was not ok");
  return res.json();
}

export async function fetchToken(username: string, password: string) {
  const params = new URLSearchParams();
  params.append("username", username);
  params.append("password", password);
  params.append("grant_type", "password");

  const response = await fetch(`${API_URL}/token/`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: params,
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
}

export async function fetchChart(symbol: string, chart_type: "revenue-vs-earnings" | "analyst-recommendations") {
  const res = await fetchClient(`${API_URL}/charts/${chart_type}?symbol=${symbol}`, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (!res.ok) throw new Error("Network response was not ok");
  return res.json();
}

export async function fetchTickerSummary(symbol: string) {
  const res = await fetchClient(`${API_URL}/tickers/${symbol}`, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  if (!res.ok) throw new Error("Network response was not ok");
  return res.json();
}
