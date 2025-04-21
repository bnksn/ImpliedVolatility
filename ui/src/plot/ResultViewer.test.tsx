import { render, screen } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import "@testing-library/jest-dom";
import ResultViewer from "./ResultViewer";
import { slicePlot } from "./PlotDropdownOptions";
import { fireEvent } from "@testing-library/dom";

import VolSurface from "../types/VolSurface";

vi.mock("./SurfacePlot", () => ({
  default: vi.fn(() => <div data-testid="surface-plot"></div>),
}));
vi.mock("./SlicePlot", () => ({
  default: vi.fn(() => <div data-testid="slice-plot"></div>),
}));

describe("ResultViewer Component", () => {
  const volSurface = {} as VolSurface;

  it("initially renders the SurfacePlot component with the default selectedPlot", () => {
    render(<ResultViewer volSurface={volSurface} />);
    const surfacePlotElement = screen.getByTestId("surface-plot");
    expect(surfacePlotElement).toBeInTheDocument();
  });

  it("renders the SlicePlot component when slicePlot is selected", () => {
    render(<ResultViewer volSurface={volSurface} />);
    const dropdownElement = screen.getByTestId("plot-dropdown-select");
    fireEvent.change(dropdownElement, { target: { value: slicePlot } });
    const slicePlotElement = screen.getByTestId("slice-plot");
    expect(slicePlotElement).toBeInTheDocument();
  });

  it("does not render SurfacePlot when slicePlot is selected", () => {
    render(<ResultViewer volSurface={volSurface} />);
    const dropdownElement = screen.getByTestId("plot-dropdown-select");
    fireEvent.change(dropdownElement, { target: { value: slicePlot } });
    const surfacePlotElement = screen.queryByTestId("surface-plot");
    expect(surfacePlotElement).toBeNull();
  });
});
