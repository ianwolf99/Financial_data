
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define the list of cryptocurrencies to visualize
cryptos = ["bitcoin", "ethereum", "cardano", "binancecoin", "dogecoin"]

# Define the API endpoint and parameters
api_endpoint = "https://api.coingecko.com/api/v3/coins/markets"
api_params = {
    "vs_currency": "usd",
    "ids": ",".join(cryptos),
    "order": "market_cap_desc",
    "per_page": "100",
    "page": "1",
    "sparkline": "false",
}

# Send the API request and get the response
response = requests.get(api_endpoint, params=api_params)
data = response.json()

# Extract the data for each cryptocurrency
crypto_data = {}
for item in data:
    crypto_data[item["id"]] = {
        "prices": item["sparkline_in_7d"]["price"],
        "name": item["name"],
        "symbol": item["symbol"],
    }

# Define the x-axis data as dates
days = len(crypto_data[cryptos[0]]["prices"])
dates = [datetime.today() - timedelta(days=x) for x in range(days)]
dates.reverse()

# Plot the data for each cryptocurrency in different types of charts
for crypto in cryptos:
    # Get the price data for the cryptocurrency
    prices = crypto_data[crypto]["prices"]
    
    # Create a figure and axes for the chart
    fig, ax = plt.subplots()
    
    # Plot a line chart of the cryptocurrency's price over time
    ax.plot(dates, prices)
    ax.set_title(f"{crypto_data[crypto]['name']} ({crypto_data[crypto]['symbol'].upper()}) Price Chart")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    
    # Save the chart as a PNG image
    fig.savefig(f"{crypto}.png")

    # Create a bar chart of the cryptocurrency's price changes over time
    fig, ax = plt.subplots()
    
    price_changes = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    ax.bar(dates[1:], price_changes)
    ax.set_title(f"{crypto_data[crypto]['name']} ({crypto_data[crypto]['symbol'].upper()}) Price Change Chart")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price Change (USD)")
    
    # Save the chart as a PNG image
    fig.savefig(f"{crypto}_changes.png")

    # Create a scatter plot of the cryptocurrency's price over time
    fig, ax = plt.subplots()
    
    ax.scatter(dates, prices)
    ax.set_title(f"{crypto_data[crypto]['name']} ({crypto_data[crypto]['symbol'].upper()}) Price Scatter Plot")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    
    # Save the chart as a PNG image
    fig.savefig(f"{crypto}_scatter.png")

    # Create a candlestick chart of the cryptocurrency's price over time
    fig, ax = plt.subplots()
    
    candlestick_data = [(dates[i], prices[i], prices[i], prices[i], prices[i+1]) for i in range(len(prices)-1)]
    ax.candlestick(candlestick_data, width=0.5)
    ax.set_title(f"{crypto_data[crypto]['name']} ({crypto_data[crypto]['symbol'].upper
