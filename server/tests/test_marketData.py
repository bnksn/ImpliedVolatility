import pytest
from unittest import mock
from freezegun import freeze_time
import yfinance as yf
import server.constants as constants
from server.marketData import getSlices, isValidTicker


@pytest.fixture
def mock_ticker():
    mock_ticker = mock.MagicMock(spec=yf.Ticker)
    mock_ticker.options = ["2025-05-15", "2025-06-19"]

    mock_option_chain_result = mock.MagicMock()
    mock_option_chain_result.calls = mock.MagicMock()
    mock_option_chain_result.calls.iterrows = mock.MagicMock(
        return_value=[
            (0, {constants.yfinanceStrikeKey: 100.0, constants.yfinanceImpliedVolatilityKey: 0.20}),
            (1, {constants.yfinanceStrikeKey: 105.0, constants.yfinanceImpliedVolatilityKey: 0.22}),
        ]
    )

    mock_ticker.option_chain.return_value = mock_option_chain_result

    return mock_ticker


@freeze_time("2025-05-01")
def test_getSlices(mock_ticker):
    slices = getSlices(mock_ticker)

    assert 14 in slices
    assert len(slices[14]) == 2
    assert 49 in slices
    assert len(slices[49]) == 2


def test_isValidTicker_valid(monkeypatch):
    mock_ticker = mock.MagicMock(spec=yf.Ticker)
    mock_ticker.info = {"symbol": "AAPL", "shortName": "Apple Inc", constants.yfinanceCurrencyKey: "USD"}
    mock_ticker.history.return_value.empty = False
    monkeypatch.setattr(yf, "Ticker", mock.MagicMock(return_value=mock_ticker))
    assert isValidTicker("AAPL")


def test_isValidTicker_invalid(monkeypatch):
    mock_ticker = mock.MagicMock(spec=yf.Ticker)
    mock_ticker.info = {"symbol": None, "shortName": "Apple Inc", constants.yfinanceCurrencyKey: "USD"}
    monkeypatch.setattr(yf, "Ticker", mock.MagicMock(return_value=mock_ticker))
    assert not isValidTicker("INVALID")


def test_isValidTicker_exception(monkeypatch):
    monkeypatch.setattr(yf, "Ticker", mock.MagicMock(side_effect=Exception("API Error")))
    assert not isValidTicker("ERROR")
