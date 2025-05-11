import yfinance as yf
import matplotlib.pyplot as plt

# Fetch Bitcoin data using yfinance
btc_data = yf.download('BTC-USD', start='2020-01-01', end='2025-01-01')

# Plot the closing price of Bitcoin
plt.figure(figsize=(10,6))
plt.plot(btc_data['Close'], label='BTC-USD Closing Price', color='blue')
plt.title('Bitcoin Price (BTC) over Time')
plt.xlabel('Date')
plt.ylabel('Price in USD')
plt.legend(loc='upper left')
plt.grid(True)

# Explicitly show the plot
plt.show()
