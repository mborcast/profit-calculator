import pytest

from datetime import datetime
from calculator.cagr import CAGR
from calculator.utils import AVERAGE_DAYS_IN_YEAR

START_DATE = "2020-01-01"
END_DATE = "2023-01-01"

@pytest.fixture
def sample_cagr():
    return CAGR(1000, 2000, START_DATE, END_DATE)


def test_can_calculate_cagr(sample_cagr):
    expected_years = (datetime(2023, 1, 1) - datetime(2020, 1, 1)).days / AVERAGE_DAYS_IN_YEAR
    expected_cagr = (2000 / 1000) ** (1 / expected_years) - 1

    assert sample_cagr.cagr == pytest.approx(expected_cagr, rel=1e-6)


def test_can_calculate_annualized_return(sample_cagr):
    expected_return = sample_cagr.cagr * 100
    assert expected_return == pytest.approx(sample_cagr.annualized_return(), rel=1e-6)


def test_raises_value_error_when_same_start_end_date():
    with pytest.raises(ValueError, match="Start and end dates are the same"):
        CAGR(1000, 2000, START_DATE, START_DATE)


def test_can_calculate_negative_growth():
    cagr = CAGR(2000, 1000, START_DATE, END_DATE)
    assert cagr.cagr < 0


def test_raises_zero_division_error_when_beginning_value_is_zero():
    with pytest.raises(ValueError, match="Beginning value cannot be zero"):
        CAGR(0, 1000, START_DATE, END_DATE)


def test_can_calculate_period_years(sample_cagr):
    expected_years = (datetime(2023, 1, 1) - datetime(2020, 1, 1)).days / AVERAGE_DAYS_IN_YEAR
    assert expected_years == pytest.approx(sample_cagr.period_years, rel=1e-6)

