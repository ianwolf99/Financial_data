import yfinance as yf
import pandas as pd
import numpy as np
import ta
import matplotlib.pyplot as plt

# Define the ticker symbol and timeframe
ticker = "WBTC-USD"
timeframe = "1d"

# Fetch historical data
data = yf.download(tickers=ticker, period="1wk", interval=timeframe)

# Calculate indicators
data["MACD"] = ta.trend.macd(data["Close"])
data["MACD Signal"] = ta.trend.macd_signal(data["Close"])
data["MACD Histogram"] = ta.trend.macd_diff(data["Close"])
data["StochRSI"] = ta.momentum.stochrsi(data["Close"])

# Define the trading strategy
data["Signal"] = 0  # 0: No signal, 1: Buy, -1: Sell

# Generate buy signals
data.loc[
    (data["MACD"] > data["MACD Signal"]) & (data["StochRSI"] < 0.2),
    "Signal"
] = 1

# Generate sell signals
data.loc[
    (data["MACD"] < data["MACD Signal"]) & (data["StochRSI"] > 0.8),
    "Signal"
] = -1

# Plotting the prices and indicators
plt.figure(figsize=(10, 6))

# Plotting the close prices
plt.plot(data.index, data["Close"], label="Close")

# Plotting MACD and Signal line
plt.plot(data.index, data["MACD"], label="MACD")
plt.plot(data.index, data["MACD Signal"], label="MACD Signal")

# Filling colors between MACD and Signal line
plt.fill_between(data.index, data["MACD"], data["MACD Signal"], where=(data["MACD"] >= data["MACD Signal"]), facecolor='green', alpha=0.2)
plt.fill_between(data.index, data["MACD"], data["MACD Signal"], where=(data["MACD"] < data["MACD Signal"]), facecolor='red', alpha=0.2)

# Plotting the Stochastic RSI
plt.plot(data.index, data["StochRSI"], label="StochRSI")

# Adding buy and sell signals
buy_signals = data[data["Signal"] == 1]
sell_signals = data[data["Signal"] == -1]
plt.scatter(
    buy_signals.index,
    buy_signals["Close"],
    marker="^",
    color="green",
    label="Buy Signal"
)
plt.scatter(
    sell_signals.index,
    sell_signals["Close"],
    marker="v",
    color="red",
    label="Sell Signal"
)

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Trading Strategy - WBTC/USDC")
plt.legend()
plt.grid(True)
plt.show()
