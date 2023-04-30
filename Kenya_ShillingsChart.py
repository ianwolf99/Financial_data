

import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Coinbase API URL
base_url = "https://api.coinbase.com/v2/"

# Cryptocurrency symbols and names
crypto_data = {"BTC": "Bitcoin", "ETH": "Ethereum", "LTC": "Litecoin"}

# Currency symbol and name
currency_data = {"KES": "Kenyan Shilling"}

# API key
api_key = "<your_api_key>"

# Get current prices for cryptocurrencies in KES
def get_crypto_prices():
    prices = {}
    for symbol, name in crypto_data.items():
        url = base_url + "prices/" + symbol + "-KES/spot"
        headers = {"Authorization": "Bearer " + api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            prices[name] = float(response.json()["data"]["amount"])
    return prices

# Get historical prices for cryptocurrencies in KES
def get_crypto_historical_prices(symbol, start_date, end_date):
    url = base_url + "prices/" + symbol + "-KES/history"
    params = {"start": start_date, "end": end_date}
    headers = {"Authorization": "Bearer " + api_key}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        return None

# Plot bar chart for current prices
def plot_bar_chart(prices):
    fig, ax = plt.subplots()
    ax.bar(prices.keys(), prices.values())
    ax.set_title("Current Prices for Cryptocurrencies")
    ax.set_ylabel("KES")
    plt.show()

# Plot scatter plot for historical prices
def plot_scatter_plot(prices):
    fig, ax = plt.subplots()
    for symbol, data in prices.items():
        dates = [datetime.strptime(d["time"], "%Y-%m-%dT%H:%M:%S.%fZ") for d in data]
        values = [float(d["price"]) for d in data]
        ax.scatter(dates, values, label=symbol)
    ax.set_title("Historical Prices for Cryptocurrencies")
    ax.set_xlabel("Date")
    ax.set_ylabel("KES")
    ax.legend()
    plt.show()

# Plot candlestick chart for historical prices
def plot_candlestick_chart(prices):
    fig, ax = plt.subplots()
    for symbol, data in prices.items():
        dates = [datetime.strptime(d["time"], "%Y-%m-%dT%H:%M:%S.%fZ") for d in data]
        opens = [float(d["open"]) for d in data]
        highs = [float(d["high"]) for d in data]
        lows = [float(d["low"]) for d in data]
        closes = [float(d["close"]) for d in data]
        ax.plot_date(dates, closes, "-", label=symbol)
        ax.fill_between(dates, opens, closes, where=closes>=opens, facecolor="green", alpha=0.5)
        ax.fill_between(dates, opens, closes, where=closes<opens, facecolor="red", alpha=0.5)
    ax.set_title("Historical Prices for Cryptocurrencies")
    ax
