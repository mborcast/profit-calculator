from calculator.portfolio import Portfolio
from calculator.stock import Stock
from calculator.time_series import TimeSeries


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

rows = [
    ["From date", profit.start_date.strftime("%Y-%m-%d")],
    ["To date", profit.end_date.strftime("%Y-%m-%d")],
    ["N", f"{profit.period_years:.4f} years"],
    ["Start Value", f"${profit.beginning_value:.2f}"],
    ["Ending Value", f"${profit.ending_value:.2f}"],
    ["Profit (CAGR)", f"{profit.cagr:.6f}"],
    ["Annualized Return (%)", f"{profit.annualized_return():.2f}%"]
]

column_widths = [max(len(str(item)) for item in column) for column in zip(*rows)]

for row in rows:
    print(f"{row[0]:<{column_widths[0]}}  {row[1]:<{column_widths[1]}}")