import pandas as pd
import matplotlib.pyplot as plt

# List of stock tickers
tickers = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA', 'TSLA']

# Create a DataFrame to hold daily returns
returns_df = pd.DataFrame()

# Read daily returns from each metrics CSV
for ticker in tickers:
    df = pd.read_csv(f'{ticker}_with_metrics.csv', parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    returns_df[ticker] = df['Daily Return']

# Plot all daily returns
plt.figure(figsize=(14, 6))
for ticker in tickers:
    plt.plot(returns_df.index, returns_df[ticker], label=ticker)

plt.title('Daily Returns of All Stocks')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('All_Stocks_Daily_Returns.png')
plt.show()
