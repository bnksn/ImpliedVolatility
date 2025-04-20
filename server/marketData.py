import yfinance as yf  # type: ignore
from server.volSurface import VolSurface
import numpy as np
import logging
import server.constants as constants
from server.dateUtils import convertMaturityToDays
from server.volSurfaceUtils import buildInterpolationAxes, interpolateVolatility

logger = logging.getLogger(__name__)


def getSlices(stock: yf.Ticker) -> dict[int, list[tuple[float, float]]]:
    slices: dict[int, list[tuple[float, float]]] = {}

    for maturity in stock.options:
        asDays = convertMaturityToDays(maturity)
        for _, call in stock.option_chain(maturity).calls.iterrows():
            strike = call[constants.yfinanceStrikeKey]
            impliedVolatility = call[constants.yfinanceImpliedVolatilityKey]
            slices.setdefault(asDays, []).append((strike, impliedVolatility))

    return slices


def getVolSurface(ticker: str) -> VolSurface:
    stock = yf.Ticker(ticker)
    slices = getSlices(stock)
    ccy = stock.info[constants.yfinanceCurrencyKey]

    # Build 1d lists for each of the x, y, and z axes
    strikes1d = []
    daysUntilMaturity1d = []
    vols1d = []
    for day, strikeVolPairs in slices.items():
        for strike, vol in strikeVolPairs:
            strikes1d.append(strike)
            daysUntilMaturity1d.append(day)
            vols1d.append(vol)

    # Build x and y axes for the 2D interpolation grid
    strikeAxis, daysToMaturityAxis = buildInterpolationAxes(strikes1d, daysUntilMaturity1d)
    strikeMaturityPoints = np.array(
        [strikes1d, daysUntilMaturity1d]
    ).T  # Each row is a point [strike, maturity] in the grid
    vols2d = interpolateVolatility(strikeAxis, daysToMaturityAxis, strikeMaturityPoints, vols1d)

    return VolSurface(ticker, strikeAxis, daysToMaturityAxis, vols2d, slices, ccy)


def isValidTicker(ticker: str) -> bool:
    try:
        info = yf.Ticker(ticker).info
        return (
            "symbol" in info
            and info["symbol"] is not None
            and ("shortName" in info or "longName" in info or "exchange" in info)
            and not yf.Ticker(ticker).history(period="1d").empty
        )
    except Exception:
        return False
