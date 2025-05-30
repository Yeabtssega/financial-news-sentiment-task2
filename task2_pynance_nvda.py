import pandas as pd
import numpy as np

# Load AAPL CSV (you can change to AMZN, TSLA etc.)
data = pd.read_csv('AAPL.csv')

# Calculate daily returns
data['Daily Return'] = data['Close'].pct_change()

# Calculate 20-day rolling volatility
data['Rolling Volatility'] = data['Daily Return'].rolling(window=20).std()

# Show last few rows
print(data[['Date', 'Close', 'Daily Return', 'Rolling Volatility']].tail())

# Save to a new CSV
data.to_csv('AAPL_with_metrics.csv', index=False)
