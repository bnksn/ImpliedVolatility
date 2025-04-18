import Plot from "react-plotly.js";
import VolSurface from "../types/VolSurface";
import { PlotType } from "plotly.js";
import "./Plot.css";

interface SurfacePlotProps {
  volSurface: VolSurface;
  type: PlotType;
}

export default function SurfacePlot(surfacePlotProps: SurfacePlotProps) {
  return (
    <div className="plot-container">
      <Plot
        data={[
          {
            type: surfacePlotProps.type,
            x: surfacePlotProps.volSurface.strikeAxis,
            y: surfacePlotProps.volSurface.daysToMaturityAxis,
            z: surfacePlotProps.volSurface.vols2d,
            colorscale: "Viridis",
          },
        ]}
        layout={{
          title: {
            text: `Implied Volatility Surface (${surfacePlotProps.volSurface.ticker})`,
          },
          scene: {
            xaxis: {
              title: {
                text: `Strike Price (${surfacePlotProps.volSurface.ccy})`,
              },
            },
            yaxis: {
              title: { text: "Maturity (days)" },
            },
            zaxis: {
              title: { text: "Implied Volatility (%)" },
            },
          },
        }}
        style={{ width: "100%", height: "100%" }}
      />
    </div>
  );
}
