import pytest

from calculator.cagr import CAGR
from calculator.portfolio import Portfolio
from calculator.stock import Stock
from calculator.time_series import TimeSeries

def test_can_calculate_total_profit():
    start_date = "2023-12-31"
    end_date = "2024-06-30"

    aapl_prices = TimeSeries({"2023-12-31": 192.53, "2024-06-30": 210.62})
    goog_prices = TimeSeries({"2023-12-31": 140.93, "2024-06-30": 183.42})

    aapl = Stock("AAPL", aapl_prices)
    goog = Stock("GOOG", goog_prices)

    # 2023-12-31: 192.53 + 140.93 = 333.46
    # 2024-06-30: 210.62 + 183.42 = 394.04
    # 394.04 - 333.46 = 60.58
    expected_total_profit = 60.58

    portfolio = Portfolio([aapl, goog])
    total_profit = portfolio.total_profit(start_date, end_date)

    assert total_profit == pytest.approx(expected_total_profit, rel=1e-6)


def test_can_calculate_profit_as_cagr():
    start_date = "2023-12-31"
    end_date = "2024-06-30"

    aapl_prices = TimeSeries({"2023-12-31": 192.53, "2024-06-30": 210.62})
    goog_prices = TimeSeries({"2023-12-31": 140.93, "2024-06-30": 183.42})

    aapl = Stock("AAPL", aapl_prices)
    goog = Stock("GOOG", goog_prices)

    # 2023-12-31: 192.53 + 140.93 = 333.46
    # 2024-06-30: 210.62 + 183.42 = 394.04
    expected_cagr = CAGR(333.46, 394.04, start_date, end_date)

    portfolio = Portfolio([aapl, goog])
    profit = portfolio.profit(start_date, end_date)

    assert profit.cagr == pytest.approx(expected_cagr.cagr, rel=1e-6)
