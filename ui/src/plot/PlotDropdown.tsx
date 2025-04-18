import { plotDropdownOptions } from "./PlotDropdownOptions";

interface PlotDropdownProps {
  selectedPlot: string;
  setSelectedPlot: (plot: string) => void;
}

export default function PlotDropdown(plotDropdownProps: PlotDropdownProps) {
  return (
    <div>
      <select
        value={plotDropdownProps.selectedPlot}
        onChange={(event: React.ChangeEvent<HTMLSelectElement>) => {
          plotDropdownProps.setSelectedPlot(event.target.value);
        }}
      >
        {plotDropdownOptions.map((option) => (
          <option value={option}>{option}</option>
        ))}
      </select>
    </div>
  );
}
