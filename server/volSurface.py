class VolSurface:
    def __init__(
        self,
        ticker: str,
        strikeAxis: list[float],
        daysToMaturityAxis: list[int],
        vols2d: list[list[float]],
        slices: dict[
            int, list[tuple[float, float]]
        ],  # Maps maturity in days to a list of tuples (strike, impliedVolatility)
        ccy: str,
    ):
        self.ticker = ticker
        self.strikeAxis = strikeAxis
        self.daysToMaturityAxis = daysToMaturityAxis
        self.vols2d = vols2d
        self.slices = slices
        self.ccy = ccy

    def toDict(self) -> dict:
        return {
            "ticker": self.ticker,
            "strikeAxis": self.strikeAxis,
            "daysToMaturityAxis": self.daysToMaturityAxis,
            "vols2d": self.vols2d,
            "slices": self.slices,
            "ccy": self.ccy,
        }
