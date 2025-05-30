import pandas as pd

# Load AMZN data
data = pd.read_csv('AMZN.csv')

# Calculate Daily Return and Rolling Volatility
data['Daily Return'] = data['Close'].pct_change()
data['Rolling Volatility'] = data['Daily Return'].rolling(window=20).std()

# Save result
data.to_csv('AMZN_with_metrics.csv', index=False)
print("Saved AMZN_with_metrics.csv")
