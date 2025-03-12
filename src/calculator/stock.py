from typing import Optional

from calculator.exceptions import StockPriceNotFoundError
from calculator.time_series import TimeSeries

class Stock:
    def __init__(self, symbol: str, time_series: TimeSeries) -> None:
        """Initializes the stock with its symbol and associated time series."""
        self.__symbol: str = symbol  # Private attribute
        self.__time_series: TimeSeries = time_series  # Private attribute

    @property
    def symbol(self) -> str:
        """Property getter for the list of stocks in the portfolio."""
        return self.__symbol

    def price(self, date: str) -> Optional[float]:
        """Returns the price of the stock for the given date.
        If price is not found, raises StockPriceNotFoundError."""
        try:
            return self.__time_series.price_at_date(date)
        except ValueError:
            raise StockPriceNotFoundError(self.__symbol, date)