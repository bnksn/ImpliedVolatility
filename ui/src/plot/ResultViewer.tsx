import { useState } from "react";
import SurfacePlot from "./SurfacePlot";
import SlicePlot from "./SlicePlot";
import "./Plot.css";
import PlotDropdown from "./PlotDropdown";
import { contourPlot, slicePlot, surfacePlot } from "./PlotDropdownOptions";
import VolSurface from "../types/VolSurface";

interface ResultViewerProps {
  volSurface: VolSurface;
}

export default function ResultViewer(resultViewerProps: ResultViewerProps) {
  const [selectedPlot, setSelectedPlot] = useState(surfacePlot);

  return (
    <div data-testid="result-viewer">
      <div className="plot-dropdown">
        <PlotDropdown
          selectedPlot={selectedPlot}
          setSelectedPlot={setSelectedPlot}
        />
      </div>
      {selectedPlot === surfacePlot && (
        <SurfacePlot
          volSurface={resultViewerProps.volSurface}
          type={surfacePlot}
        />
      )}
      {selectedPlot === contourPlot && (
        <SurfacePlot
          volSurface={resultViewerProps.volSurface}
          type={contourPlot}
        />
      )}
      {selectedPlot === slicePlot && (
        <SlicePlot volSurface={resultViewerProps.volSurface} />
      )}
    </div>
  );
}
