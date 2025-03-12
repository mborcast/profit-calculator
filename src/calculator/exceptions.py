class StockPriceNotFoundError(Exception):
    """Exception raised when the price for a stock is not available for a specific date."""

    def __init__(self, symbol: str, date: str) -> None:
        super().__init__(f"Price not available for {symbol} on {date}")
        self.symbol = symbol
        self.date = date


class MissingPriceDateError(Exception):
    """Exception raised when a stock is missing price data for a given date."""

    def __init__(self, symbol: str, date: str) -> None:
        super().__init__(f"Price not available for {symbol} on {date}")
        self.symbol = symbol
        self.date = date