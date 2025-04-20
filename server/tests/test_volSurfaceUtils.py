from server.volSurfaceUtils import buildInterpolationAxes
from unittest import mock
from server import constants


def test_buildInterpolationAxes_valid_input() -> None:
    strikes1d = [100.0, 110.0, 120.0]
    daysUntilMaturity1d = [30, 60, 90]
    with mock.patch.object(constants, "numGridAxisPoints", 5):
        strikeAxis, daysUntilMaturityAxis = buildInterpolationAxes(strikes1d, daysUntilMaturity1d)
        assert len(strikeAxis) == 5
        assert len(daysUntilMaturityAxis) == 5
        assert min(strikeAxis) == min(strikes1d)
        assert max(strikeAxis) == max(strikes1d)
        assert min(daysUntilMaturityAxis) == min(daysUntilMaturity1d)
        assert max(daysUntilMaturityAxis) == max(daysUntilMaturity1d)
        assert all(isinstance(s, float) for s in strikeAxis)
        assert all(isinstance(d, int) for d in daysUntilMaturityAxis)
