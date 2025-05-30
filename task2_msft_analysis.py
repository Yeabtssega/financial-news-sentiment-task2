import pandas as pd
import talib
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('MSFT.csv')

# Calculate indicators
data['SMA'] = talib.SMA(data['Close'], timeperiod=20)
data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
data['MACD'] = macd
data['MACD_Signal'] = macdsignal

# Plot SMA
plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['Date'], data['SMA'], label='SMA (20)', color='red')
plt.title('MSFT Stock with SMA, RSI & MACD')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.savefig('MSFT_sma_chart.png')
