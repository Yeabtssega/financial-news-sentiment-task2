import pandas as pd
import os

# Folder containing *_with_metrics.csv files
folder_path = "C:/Users/HP/Stock Analysis"

# Stock tickers you're analyzing
stock_symbols = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA', 'TSLA']

# Prepare a list to store summary data
summary_data = []

for symbol in stock_symbols:
    file_path = os.path.join(folder_path, f"{symbol}_with_metrics.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path, parse_dates=['Date'])
        
        mean_return = df['Daily Return'].mean()
        std_return = df['Daily Return'].std()

        summary_data.append({
            'Stock': symbol,
            'Mean Daily Return': mean_return,
            'Volatility (Std Dev)': std_return
        })
    else:
        print(f"File not found for {symbol}: {file_path}")

# Convert to DataFrame and save
summary_df = pd.DataFrame(summary_data)
summary_df.to_csv(os.path.join(folder_path, "Stock_Summary_Metrics.csv"), index=False)

print("Summary metrics saved to 'Stock_Summary_Metrics.csv'")
