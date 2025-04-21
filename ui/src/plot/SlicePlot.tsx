import Plot from "react-plotly.js";
import VolSurface from "../types/VolSurface";
import "./Plot.css";

interface SlicePlotProps {
  volSurface: VolSurface;
}

export default function SlicePlot(slicePlotProps: SlicePlotProps) {
  return (
    <div className="plot-container" data-testid="slice-plot">
      <Plot
        data={Object.entries(slicePlotProps.volSurface.slices).map(
          ([day, values]) => ({
            x: values.map(([strike, _]) => strike),
            y: values.map(([_, vol]) => vol),
            type: "scatter",
            mode: "lines+markers",
            name: `${day} Days`,
          }),
        )}
        layout={{
          title: {
            text: `Implied Volatility vs Strike (${slicePlotProps.volSurface.ticker})`,
          },
          xaxis: {
            title: { text: `Strike Price (${slicePlotProps.volSurface.ccy})` },
          },
          yaxis: { title: { text: "Implied Volatility (%)" } },
          legend: { title: { text: "Maturity (days)" } },
        }}
        style={{ width: "100%", height: "100%" }}
      />
    </div>
  );
}
