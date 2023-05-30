import yfinance as yf
import pandas as pd
import numpy as np
import ta
import matplotlib.pyplot as plt

# Define the ticker symbol and timeframe
ticker = "WBTC-USD"
timeframe = "1d"

# Fetch historical data
data = yf.download(tickers=ticker, period="1y", interval=timeframe)

# Calculate indicators
data["SMA_20"] = ta.trend.sma_indicator(data["Close"], window=20)
data["SMA_50"] = ta.trend.sma_indicator(data["Close"], window=50)
data["RSI"] = ta.momentum.rsi(data["Close"])

# Define the trading strategy
data["Signal"] = 0  # 0: No signal, 1: Buy, -1: Sell

# Generate buy signals
data.loc[
    (data["SMA_20"] > data["SMA_50"]) & (data["RSI"] < 30),
    "Signal"
] = 1

# Generate sell signals
data.loc[
    (data["SMA_20"] < data["SMA_50"]) & (data["RSI"] > 70),
    "Signal"
] = -1

# Calculate the positions
data["Position"] = data["Signal"].diff()

# Calculate the returns
data["Return"] = data["Close"].pct_change()

# Calculate the strategy returns
data["StrategyReturn"] = data["Position"] * data["Return"]

# Calculate the cumulative returns
data["CumulativeReturn"] = (1 + data["StrategyReturn"]).cumprod()

# Plot the cumulative returns
plt.figure(figsize=(10, 6))
plt.plot(data["CumulativeReturn"])
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.title("Cumulative Return of the Trading Strategy")
plt.grid(True)
plt.show()
