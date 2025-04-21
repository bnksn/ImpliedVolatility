import { plotDropdownOptions } from "./PlotDropdownOptions";

interface PlotDropdownProps {
  selectedPlot: string;
  setSelectedPlot: (plot: string) => void;
}

export default function PlotDropdown(plotDropdownProps: PlotDropdownProps) {
  return (
    <div data-testid="plot-dropdown">
      <select
        data-testid="plot-dropdown-select"
        value={plotDropdownProps.selectedPlot}
        onChange={(event: React.ChangeEvent<HTMLSelectElement>) => {
          plotDropdownProps.setSelectedPlot(event.target.value);
        }}
      >
        {plotDropdownOptions.map((option) => (
          <option
            key={option}
            value={option}
            data-testid="plot-dropdown-option"
          >
            {option}
          </option>
        ))}
      </select>
    </div>
  );
}
