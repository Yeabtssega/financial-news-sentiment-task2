import pandas as pd

# Load GOOG data
data = pd.read_csv('GOOG.csv')

# Calculate Daily Return and Rolling Volatility
data['Daily Return'] = data['Close'].pct_change()
data['Rolling Volatility'] = data['Daily Return'].rolling(window=20).std()

# Save result
data.to_csv('GOOG_with_metrics.csv', index=False)
print("Saved GOOG_with_metrics.csv")
