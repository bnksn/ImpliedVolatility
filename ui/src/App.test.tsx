import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import "@testing-library/jest-dom";
import App from "./App";

describe("App Component", () => {
  it("renders the Form component initially", () => {
    render(<App />);
    const formElement = screen.getByTestId("form");
    expect(formElement).toBeInTheDocument();
  });

  it("does not render ResultViewer initially", () => {
    render(<App />);
    const resultViewerElement = screen.queryByTestId("result-viewer");
    expect(resultViewerElement).toBeNull();
  });
});
