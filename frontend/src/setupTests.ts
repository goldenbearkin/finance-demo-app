import { server } from "./mocks/server";
import { beforeAll, afterEach, afterAll, vi } from "vitest";
import "@testing-library/jest-dom";

vi.mock("./config", () => ({
  API_URL: "http://localhost:8000",
}));

// Setup MSW mock server
beforeAll(() => server.listen({ onUnhandledRequest: "error" }));

afterEach(() => server.resetHandlers());

afterAll(() => server.close());
