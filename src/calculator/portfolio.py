from typing import List

from calculator.cagr import CAGR
from calculator.exceptions import MissingPriceDateError, StockPriceNotFoundError
from calculator.stock import Stock


class Portfolio:
    def __init__(self, stocks: List[Stock]) -> None:
        """Initializes the portfolio with a list of stocks."""
        self.__stocks: List[Stock] = stocks

    @property
    def stocks(self) -> List[Stock]:
        """Property getter for the list of stocks in the portfolio."""
        return self.__stocks

    def total_profit(self, start_date: str, end_date: str) -> float:
        """Calculates the profit of the portfolio between two dates.
        Raises MissingPriceDateError if any price data is missing for the given dates."""
        total_profit = 0.0

        for stock in self.__stocks:
            try:
                # Check if price is available for both start_date and end_date
                start_price = stock.price(start_date)
                end_price = stock.price(end_date)

                # Calculate profit if both prices are found
                total_profit += end_price - start_price

            except StockPriceNotFoundError as e:
                raise MissingPriceDateError(stock.symbol, e.date)

        return total_profit

    def profit(self, start_date: str, end_date: str) -> CAGR:
        """Calculates the annualized return (CAGR) of the portfolio between two dates."""

        beginning_value = 0.0
        ending_value = 0.0

        for stock in self.__stocks:
            try:
                start_price = stock.price(start_date)
                end_price = stock.price(end_date)

                beginning_value += start_price
                ending_value += end_price

            except MissingPriceDateError as e:
                raise MissingPriceDateError(stock.symbol, e.date)

        if beginning_value == 0:
            return 0.0

        return CAGR(beginning_value, ending_value, start_date, end_date)
