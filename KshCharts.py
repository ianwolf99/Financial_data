
import requests
import pandas as pd
import plotly.graph_objects as go

# Set up the CoinGecko API endpoint
base_url = "https://api.coingecko.com/api/v3"
endpoint = "/coins/markets"

# Set up parameters for the API request
vs_currency = "KES"
ids = ["bitcoin", "ethereum", "usd-coin"]
params = {
    "vs_currency": vs_currency,
    "ids": ids,
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": False
}

# Send a GET request to the API endpoint with the parameters
response = requests.get(base_url + endpoint, params=params)

# Convert the response JSON data to a pandas dataframe
df = pd.json_normalize(response.json())

# Select only the relevant columns
df = df[["id", "name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h", "sparkline_in_7d.price"]]

# Convert the timestamp column to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

# Define the chart data and layout for the line chart
line_data = []
for id in ids:
    line_trace = go.Scatter(x=df[df["id"]==id]["timestamp"], y=df[df["id"]==id]["current_price"], name=id.capitalize())
    line_data.append(line_trace)
line_layout = go.Layout(title="Cryptocurrency Prices Over Time", xaxis_title="Time", yaxis_title="Price (KES)")

# Define the chart data and layout for the scatter plot
scatter_data = []
for id in ids:
    scatter_trace = go.Scatter(x=df[df["id"]==id]["market_cap"], y=df[df["id"]==id]["price_change_percentage_24h"], name=id.capitalize(), mode="markers", marker_size=10)
    scatter_data.append(scatter_trace)
scatter_layout = go.Layout(title="Cryptocurrency Market Cap vs. Price Change (24h)", xaxis_title="Market Cap (KES)", yaxis_title="Price Change (24h)")

# Define the chart data and layout for the candlestick chart
candlestick_data = []
for id in ids:
    candlestick_trace = go.Candlestick(x=df[df["id"]==id]["timestamp"], open=df[df["id"]==id]["current_price"], high=df[df["id"]==id]["high_24h"], low=df[df["id"]==id]["low_24h"], close=df[df["id"]==id]["current_price"], name=id.capitalize())
    candlestick_data.append(candlestick_trace)
candlestick_layout = go.Layout(title="Cryptocurrency Candlestick Chart", xaxis_title="Time", yaxis_title="Price (KES)")

# Create the line chart, scatter plot, and candlestick chart
line_chart = go.Figure(data=line_data, layout=line_layout)
scatter_plot = go.Figure(data=scatter_data, layout=scatter_layout)
candlestick_chart = go.Figure(data=candlestick_data, layout=candlestick_layout)

# Show the charts
line_chart.show()
scatter_plot.show()
candlestick_chart.show()
