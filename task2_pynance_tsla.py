import pandas as pd

data = pd.read_csv('TSLA.csv')
data['Daily Return'] = data['Close'].pct_change()
data['Rolling Volatility'] = data['Daily Return'].rolling(window=20).std()
data.to_csv('TSLA_with_metrics.csv', index=False)
df = pd.read_csv('TSLA.csv')
