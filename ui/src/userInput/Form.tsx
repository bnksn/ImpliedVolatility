import { useState } from "react";
import VolSurface from "../types/VolSurface";
import "./Form.css";

interface FormProps {
  setVolSurface: (volSurface: VolSurface) => void;
}

export default function Form(formProps: FormProps) {
  const [ticker, setTicker] = useState<string>();
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const response = await fetch(
        `http://localhost:5000/getImpliedSurface?ticker=${ticker}`,
      );
      if (!response.ok) {
        const errorJson = await response.json(); // Parse the response JSON
        throw new Error(`Error: ${errorJson.error || "Unknown error"}`);
      }

      formProps.setVolSurface(await response.json());
    } catch (error: any) {
      alert(error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} data-testid="form">
      <label>
        Ticker:
        <input
          data-testid="ticker-input"
          type="text"
          value={ticker}
          onChange={(e) => setTicker(e.target.value)}
        />
      </label>
      <button type="submit" disabled={isLoading} data-testid="ticker-button">
        {isLoading ? "Retrieving Surface" : "Get Surface"}
      </button>
    </form>
  );
}
