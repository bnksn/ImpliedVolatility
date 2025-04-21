import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import "@testing-library/jest-dom";
import {
  contourPlot,
  plotDropdownOptions,
  surfacePlot,
} from "./PlotDropdownOptions";
import PlotDropdown from "./PlotDropdown";

describe("PlotDropdown Component", () => {
  it("renders the select element with the correct initial value", () => {
    const selectedPlot = surfacePlot;
    render(
      <PlotDropdown selectedPlot={selectedPlot} setSelectedPlot={vi.fn()} />,
    );

    const selectElement = screen.getByTestId("plot-dropdown-select");
    expect(selectElement).toBeInTheDocument();
    expect((selectElement as HTMLSelectElement).value).toBe(selectedPlot);
  });

  it("renders all the options from plotDropdownOptions", () => {
    render(
      <PlotDropdown selectedPlot={surfacePlot} setSelectedPlot={vi.fn()} />,
    );

    const options = screen.getAllByTestId("plot-dropdown-option");

    expect(options.length).toBe(plotDropdownOptions.length);
    options.forEach((option, index) => {
      expect((option as HTMLOptionElement).value).toBe(
        plotDropdownOptions[index],
      );
      expect(option.textContent).toBe(plotDropdownOptions[index]);
    });
  });

  it("calls setSelectedPlot with the new value when the selection changes", () => {
    const selectedPlot = surfacePlot;
    const mockSetSelectedPlot = vi.fn();
    render(
      <PlotDropdown
        selectedPlot={selectedPlot}
        setSelectedPlot={mockSetSelectedPlot}
      />,
    );

    const selectElement = screen.getByTestId("plot-dropdown-select");
    const newValue = contourPlot;

    fireEvent.change(selectElement, { target: { value: newValue } });

    expect(mockSetSelectedPlot).toHaveBeenCalledTimes(1);
    expect(mockSetSelectedPlot).toHaveBeenCalledWith(newValue);
  });
});
