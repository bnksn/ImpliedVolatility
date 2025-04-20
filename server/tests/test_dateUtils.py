import pytest
from server.dateUtils import convertMaturityToDays
from freezegun import freeze_time


@freeze_time("2025-01-01")
@pytest.mark.parametrize(
    "maturity_date, expected_days",
    [
        ("2025-01-15", 14),
        ("2025-02-01", 31),
        ("2025-12-31", 364),
        ("2026-01-01", 365),
    ],
)
def test_convertMaturityToDays_future_dates(maturity_date: str, expected_days: int) -> None:
    assert convertMaturityToDays(maturity_date) == expected_days


def test_convertMaturityToDays_invalid_format() -> None:
    invalid_date_str = "15-01-2026"
    with pytest.raises(ValueError):
        convertMaturityToDays(invalid_date_str)
