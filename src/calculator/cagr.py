from datetime import datetime
from typing import Optional

from calculator.utils import AVERAGE_DAYS_IN_YEAR


class CAGR:
    def __init__(self, beginning_value: float, ending_value: float, start_date: str, end_date: str) -> None:
        """Calculates the Compound Annual Growth Rate (CAGR)."""
        if beginning_value == 0:
            raise ValueError("Beginning value cannot be zero")

        self.__beginning_value = beginning_value
        self.__ending_value = ending_value

        self.__start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.__end_date = datetime.strptime(end_date, "%Y-%m-%d")

        self.__period_years = (self.__end_date - self.__start_date).days / AVERAGE_DAYS_IN_YEAR

        if self.__period_years == 0:
            raise ValueError("Start and end dates are the same")

        self.__cagr = (self.__ending_value / self.__beginning_value) ** (1 / self.__period_years) - 1

    @property
    def cagr(self) -> float:
        return self.__cagr

    @property
    def beginning_value(self) -> float:
        return self.__beginning_value

    @property
    def ending_value(self) -> float:
        return self.__ending_value

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @property
    def period_years(self) -> int:
        return self.__period_years

    def annualized_return(self) -> Optional[float]:
        """Returns the annualized return as a percentage."""
        return self.__cagr * 100
