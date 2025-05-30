import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

folder_path = "C:/Users/HP/Stock Analysis"
stock_symbols = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA', 'TSLA']

returns_df = pd.DataFrame()

# Merge Daily Return columns into one DataFrame
for symbol in stock_symbols:
    file_path = os.path.join(folder_path, f"{symbol}_with_metrics.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path, parse_dates=['Date'])
        returns_df[symbol] = df['Daily Return']
    else:
        print(f"Missing file for {symbol}")

# Drop rows with NaN values
returns_df = returns_df.dropna()

# Compute correlation matrix
correlation_matrix = returns_df.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Daily Return Correlation Heatmap")
plt.tight_layout()

# Save the figure
heatmap_path = os.path.join(folder_path, "Return_Correlation_Heatmap.png")
plt.savefig(heatmap_path)
plt.close()

print(f"Heatmap saved to {heatmap_path}")
