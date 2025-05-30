import pandas as pd
import numpy as np
import os

# Folder path with the stock CSVs
folder_path = r'C:\Users\HP\Stock Analysis'

# Remaining symbols to process
symbols = ['META', 'MSFT', 'NVDA', 'TSLA']

for symbol in symbols:
    file_path = os.path.join(folder_path, f'{symbol}.csv')
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df.sort_values('Date', inplace=True)

    # Calculate Daily Return
    df['Daily Return'] = df['Adj Close'].pct_change()

    # Calculate 20-day Rolling Volatility
    df['Rolling Volatility'] = df['Daily Return'].rolling(window=20).std()

    # Save to new CSV
    output_file = os.path.join(folder_path, f'{symbol}_with_metrics.csv')
    df.to_csv(output_file, index=False)

print("✅ Metrics generated for META, MSFT, NVDA, TSLA.")
