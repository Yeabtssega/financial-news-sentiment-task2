import pandas as pd
import talib
import matplotlib.pyplot as plt

data = pd.read_csv('AMZN.csv')

data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)
data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)
data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
data['MACD'] = macd
data['MACD_Signal'] = macdsignal

plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label='Close Price')
plt.plot(data['Date'], data['SMA_20'], label='SMA 20')
plt.plot(data['Date'], data['SMA_50'], label='SMA 50')
plt.legend()
plt.title('AMZN Stock with SMA, RSI & MACD')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('AMZN_sma_chart.png')
