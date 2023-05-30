import yfinance as yf
import pandas as pd
import numpy as np
import ta
import matplotlib.pyplot as plt

# Define the ticker symbol and timeframe
ticker = "WBTC-USD"
timeframe = "1d"

# Fetch historical data
data = yf.download(tickers=ticker, period="6mo", interval=timeframe)

# Calculate indicators
data["EMA200"] = ta.trend.ema_indicator(data["Close"], window=200)
data["EMA9"] = ta.trend.ema_indicator(data["Close"], window=9)
data["StochRSI"] = ta.momentum.stochrsi(data["Close"])

# Define the trading strategy
data["Signal"] = 0  # 0: No signal, 1: Buy, -1: Sell

# Generate buy signals
data.loc[
    (data["EMA9"].shift(1) < data["EMA200"].shift(1)) & (data["EMA9"] > data["EMA200"]) & (data["StochRSI"] < 0.2),
    "Signal"
] = 1

# Generate sell signals
data.loc[
    (data["EMA9"].shift(1) > data["EMA200"].shift(1)) & (data["EMA9"] < data["EMA200"]) & (data["StochRSI"] > 0.8),
    "Signal"
] = -1

# Plotting the prices and indicators
plt.figure(figsize=(10, 6))

# Plotting the close prices
plt.plot(data.index, data["Close"], label="Close")

# Plotting EMA lines
plt.plot(data.index, data["EMA200"], label="EMA 200")
plt.plot(data.index, data["EMA9"], label="EMA 9")

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
