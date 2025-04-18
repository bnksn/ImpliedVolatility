import { useState } from "react";
import Form from "./userInput/Form";
import VolSurface from "./types/VolSurface";
import ResultViewer from "./plot/ResultViewer";
import "./global.css";

export default function App() {
  const [volSurface, setVolSurface] = useState<VolSurface>();

  return (
    <div style={{ padding: "10px" }}>
      <Form setVolSurface={setVolSurface} />
      {volSurface && <ResultViewer volSurface={volSurface} />}
    </div>
  );
}
