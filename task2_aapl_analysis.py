import pandas as pd
import matplotlib.pyplot as plt
import talib

# Load the AAPL data
data = pd.read_csv('AAPL.csv')

# Convert 'Date' column to datetime and set as index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Calculate SMA (Simple Moving Average)
data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)

# Calculate RSI
data['RSI'] = talib.RSI(data['Close'], timeperiod=14)

# Calculate MACD
macd, macdsignal, macdhist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
data['MACD'] = macd
data['MACD_Signal'] = macdsignal

# Plotting
plt.figure(figsize=(12, 8))

# Price and SMA
plt.subplot(3, 1, 1)
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA_20'], label='SMA 20')
plt.title('AAPL Stock with SMA, RSI & MACD')
plt.legend()

# RSI
plt.subplot(3, 1, 2)
plt.plot(data['RSI'], label='RSI', color='purple')
plt.axhline(70, color='red', linestyle='--')
plt.axhline(30, color='green', linestyle='--')
plt.title('Relative Strength Index')

# MACD
plt.subplot(3, 1, 3)
plt.plot(data['MACD'], label='MACD', color='blue')
plt.plot(data['MACD_Signal'], label='Signal', color='orange')
plt.title('MACD')

plt.tight_layout()
plt.savefig('AAPL_sma_chart.png')
