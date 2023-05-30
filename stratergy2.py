import yfinance as yf
import ta
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define the start and end dates for the one-week period
end_date = datetime.now().date()
start_date = end_date - timedelta(days=150)

# Fetch Bitcoin data using yfinance
btc_data = yf.download("BTC-USD", start=start_date, end=end_date)

# Calculate RSI
rsi = ta.momentum.RSIIndicator(btc_data['Close'], window=14).rsi()

# Calculate MACD
macd = ta.trend.MACD(btc_data['Close'], window_slow=26, window_fast=12).macd()

# Calculate Stochastic
stoch = ta.momentum.StochasticOscillator(btc_data['High'], btc_data['Low'], btc_data['Close'], window=14).stoch()

# Determine divergences
rsi_sma = ta.trend.sma_indicator(rsi, window=14)
rsi_divergence = rsi > rsi_sma

macd_sma = ta.trend.sma_indicator(macd, window=9)
macd_divergence = macd > macd_sma

stoch_sma = ta.trend.sma_indicator(stoch, window=14)
stoch_divergence = stoch > stoch_sma

# Plotting
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True, figsize=(12, 10))

# Plot Bitcoin Close Price
ax1.plot(btc_data.index, btc_data['Close'])
ax1.set_ylabel('Price')

# Plot RSI
ax2.plot(rsi.index, rsi, color='blue')
ax2.axhline(30, color='green', linestyle='--')
ax2.axhline(70, color='red', linestyle='--')
ax2.set_ylabel('RSI')

# Plot MACD
ax3.plot(macd.index, macd, label='MACD', color='blue')
ax3.plot(macd.index, macd_sma, label='Signal', color='orange')
ax3.legend()
ax3.set_ylabel('MACD')

# Plot Stochastic
ax4.plot(stoch.index, stoch, label='Stochastic', color='blue')
ax4.axhline(20, color='green', linestyle='--')
ax4.axhline(80, color='red', linestyle='--')
ax4.set_ylabel('Stochastic')

# Determine buy/sell conditions
buy_condition = rsi_divergence & macd_divergence & stoch_divergence
sell_condition = rsi_divergence & macd_divergence & ~stoch_divergence

# Plot Buy/Sell signals
buy_indices = [i for i, signal in enumerate(buy_condition) if signal]
sell_indices = [i for i, signal in enumerate(sell_condition) if signal]
ax1.plot(btc_data.index[buy_indices], btc_data['Close'].values[buy_indices], 'g^', markersize=10, label='Buy')
ax1.plot(btc_data.index[sell_indices], btc_data['Close'].values[sell_indices], 'rv', markersize=10, label='Sell')

# Add legend and adjust layout
ax1.legend()
plt.tight_layout()

# Display the chart
plt.show()
