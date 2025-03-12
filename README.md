# Stock Portfolio Calculator

This project allows you to manage a portfolio of stocks, calculate the profit, and compute the Compound Annual Growth Rate (CAGR) of individual stocks and portfolios.

## Usage example

```python
# Create stock price series
aapl_prices = TimeSeries({"2023-12-31": 192.53, "2024-12-31": 250.42})
goog_prices = TimeSeries({"2023-12-31": 140.93, "2024-12-31": 193.13})

# Create stocks
aapl = Stock("AAPL", aapl_prices)
goog = Stock("GOOG", goog_prices)

# Create portfolio and initialize with stocks
portfolio = Portfolio([aapl, goog])

# Calculate profit
profit = portfolio.profit("2023-12-31", "2024-12-31")
```


## Classes

### 1. TimeSeries
A class representing a time series of stock prices.

**Methods:**
- `__init__(self, data: Dict[str, float])`: Initializes the time series with a dictionary of date-price pairs.
- `price_at_date(self, date: str)`: Returns the price of the stock at the given date. Raises a `ValueError` if the price is not available for that date.

---

### 2. Stock
A class representing a stock, which has a symbol and an associated time series.

**Methods:**
- `__init__(self, symbol: str, time_series: TimeSeries)`: Initializes the stock with its symbol and associated time series.
- `symbol(self)`: Property getter for the stock's symbol.
- `price(self, date: str)`: Returns the price of the stock at a given date. If not found, raises a `StockPriceNotFoundError`.

---

### 3. CAGR
A class to calculate the Compound Annual Growth Rate (CAGR) of a stock or portfolio over a specified time period.

**Methods:**
- `__init__(self, beginning_value: float, ending_value: float, start_date: str, end_date: str)`: Initializes the class with beginning and ending values, and the corresponding start and end dates.
- `cagr(self)`: Property to return the CAGR.
- `annualized_return(self)`: Returns the annualized return as a percentage.

---

### 4. Portfolio
A class representing a portfolio of multiple stocks.

**Methods:**
- `__init__(self, stocks: List[Stock])`: Initializes the portfolio with a list of stocks.
- `total_profit(self, start_date: str, end_date: str)`: Calculates the total profit of the portfolio between two dates. Raises a `MissingPriceDateError` if any price data is missing.
- `profit(self, start_date: str, end_date: str)`: Calculates the portfolio's annualized return (CAGR) between two dates.

---

## Exceptions

### StockPriceNotFoundError
This exception is raised when a stock price is not found for a given date.

### MissingPriceDateError
This exception is raised if any price data is missing for the given dates while calculating the total profit of the portfolio.

---

## Tests

The project includes tests for the classes and methods using `pytest`. The test files are located in the `tests/` directory.

### Running Tests

To run the tests, use `pytest`. You can run all tests with the following command:

```bash
pytest
```

## Requirements
Python 3.6+

Install the required dependencies using:

```bash
pip install -r requirements.txt
```