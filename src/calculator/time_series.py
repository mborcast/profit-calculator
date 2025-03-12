from typing import Dict, Optional

class TimeSeries:
    def __init__(self, data: Dict[str, float]) -> None:
        """Initializes the time series with a dictionary of date-price pairs."""
        self.__data: Dict[str, float] = data

    def price_at_date(self, date: str) -> Optional[float]:
        """Returns the price of the stock at the given date.
        Raises ValueError if price is not available."""
        if date not in self.__data:
            raise ValueError(f"Price not available on {date}")
        return self.__data[date]