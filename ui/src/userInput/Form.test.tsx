import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import "@testing-library/jest-dom";
import Form from "./Form";

describe("Form Component", () => {
  const mockSetVolSurface = vi.fn();

  it("renders the ticker input and get surface button", () => {
    render(<Form setVolSurface={mockSetVolSurface} />);
    const tickerInput = screen.getByTestId("ticker-input");
    const getSurfaceButton = screen.getByTestId("ticker-button");
    expect(tickerInput).toBeInTheDocument();
    expect(getSurfaceButton).toBeInTheDocument();
    expect(getSurfaceButton).toBeEnabled();
  });

  it("updates the ticker state when the input changes", () => {
    render(<Form setVolSurface={mockSetVolSurface} />);
    const tickerInput = screen.getByTestId("ticker-input");
    fireEvent.change(tickerInput, { target: { value: "AAPL" } });
    expect((tickerInput as HTMLInputElement).value).toBe("AAPL");
  });
});
