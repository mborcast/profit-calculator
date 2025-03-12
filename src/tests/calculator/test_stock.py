import pytest

from calculator.exceptions import StockPriceNotFoundError
from calculator.stock import Stock
from calculator.time_series import TimeSeries


@pytest.fixture
def stock():
    time_series = TimeSeries({
        "2023-01-01": 150,
        "2023-03-01": 160,
    })
    return Stock("STK", time_series)


def test_returns_price_when_value_exists(stock: Stock):
    assert stock.price("2023-01-01") == 150
    assert stock.price("2023-03-01") == 160


def test_price_raises_stock_price_not_found_error(stock: Stock):
    missing_date = "2023-02-01"

    with pytest.raises(StockPriceNotFoundError, match="Price not available for STK on 2023-02-01"):
        stock.price(missing_date)

