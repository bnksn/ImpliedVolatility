import numpy as np
import scipy.interpolate  # type: ignore
import constants


def buildInterpolationGrid(strikes1d: list[float], daysUntilMaturity1d: list[int]) -> tuple[list[float], list[int]]:
    strikeAxis = [float(s) for s in np.linspace(min(strikes1d), max(strikes1d), constants.numGridAxisPoints)]
    daysUntilMaturityAxis = [
        int(d) for d in np.linspace(min(daysUntilMaturity1d), max(daysUntilMaturity1d), constants.numGridAxisPoints)
    ]

    return strikeAxis, daysUntilMaturityAxis


def interpolateVolatility(
    strikeAxis: list[float],
    daysUntilMaturityAxis: list[int],
    strikeMaturityPoints: np.ndarray,  # 2d array of shape (num points, 2)
    vols1d: list[float],  # 1d array of shape (num points,)
) -> list[list[float]]:
    vols2d = scipy.interpolate.griddata(
        strikeMaturityPoints,
        vols1d,
        np.meshgrid(strikeAxis, daysUntilMaturityAxis),
        method=constants.interpolationMethod,
    )

    # Values outside the convex hull of our strikeMatuirty points are NaN. Convert these to None.
    return np.where(np.isnan(vols2d), None, vols2d).tolist()  # type: ignore
