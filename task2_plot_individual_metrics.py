import pandas as pd
import matplotlib.pyplot as plt

# List of stock tickers
tickers = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA', 'TSLA']

# Loop through each ticker and create plots
for ticker in tickers:
    df = pd.read_csv(f'{ticker}_with_metrics.csv', parse_dates=['Date'])
    df.set_index('Date', inplace=True)

    # Plot Daily Return
    plt.figure(figsize=(10, 4))
    plt.plot(df.index, df['Daily Return'], label='Daily Return', color='blue')
    plt.title(f'{ticker} - Daily Return')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'{ticker}_daily_return.png')
    plt.close()

    # Plot Rolling Volatility
    plt.figure(figsize=(10, 4))
    plt.plot(df.index, df['Rolling Volatility'], label='Rolling Volatility (30D)', color='orange')
    plt.title(f'{ticker} - Rolling Volatility (30 Days)')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'{ticker}_rolling_volatility.png')
    plt.close()
