import pytest
import time
from server.volCache import VolCache


@pytest.fixture
def expiration_time():
    return 1


@pytest.fixture
def volCache(expiration_time):
    return VolCache(expiration_time)


@pytest.fixture
def ticker():
    return "AAPL"


@pytest.fixture
def data():
    return {"surface": [[0.2, 0.3], [0.4, 0.5]]}


def test_initialization(volCache, expiration_time):
    assert volCache.expirationSeconds == expiration_time
    assert volCache.internalCache == {}


def test_set_and_get_hit(volCache, ticker, data):
    volCache.set(ticker, data)
    retrieved_data = volCache.get(ticker)
    assert retrieved_data == data


def test_get_miss_not_found(volCache):
    retrieved_data = volCache.get("MSFT")
    assert retrieved_data is None


def test_get_miss_expired(volCache, ticker, data, expiration_time):
    volCache.set(ticker, data)
    time.sleep(expiration_time + 0.1)
    retrieved_data = volCache.get(ticker)
    assert retrieved_data is None
