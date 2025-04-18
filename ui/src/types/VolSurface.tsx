export default interface VolSurface {
  ticker: string;
  strikeAxis: number[];
  daysToMaturityAxis: number[];
  vols2d: number[][];
  slices: Record<number, Slice>;
  ccy: string;
}

export type Slice = [number, number][];
