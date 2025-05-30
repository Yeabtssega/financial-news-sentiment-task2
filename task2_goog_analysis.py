import pandas as pd
import talib
import matplotlib.pyplot as plt

# Load GOOG stock data
data = pd.read_csv('GOOG.csv')

# Calculate SMA (Simple Moving Average)
data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)

# RSI (Relative Strength Index)
data['RSI'] = talib.RSI(data['Close'], timeperiod=14)

# MACD (Moving Average Convergence Divergence)
macd, macdsignal, macdhist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
data['MACD'] = macd
data['MACD_Signal'] = macdsignal

# Preview data
print("Data Preview:")
print(data.head())

# Plot closing price and SMA
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['SMA_20'], label='SMA 20', color='orange')
plt.title('GOOG Stock with SMA, RSI & MACD')
plt.xlabel('Days')
plt.ylabel('Price')
plt.legend()

# Save chart image
plt.savefig('GOOG_sma_chart.png')
