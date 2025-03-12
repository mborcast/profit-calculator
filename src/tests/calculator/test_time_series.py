import pytest

from calculator.time_series import TimeSeries


@pytest.fixture
def prices():
    return TimeSeries({
        "2023-01-01": 150,
        "2023-03-01": 160,
        "2023-06-01": 170
    })

def test_returns_price_when_value_exists(prices: TimeSeries):
    assert prices.price_at_date("2023-01-01") == 150
    assert prices.price_at_date("2023-03-01") == 160


def test_raises_value_error_when_date_does_not_exist(prices: TimeSeries):
    missing_date = "2023-02-01"

    with pytest.raises(ValueError, match=f"Price not available on {missing_date}"):
        prices.price_at_date(missing_date)
