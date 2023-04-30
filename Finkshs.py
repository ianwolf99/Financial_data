
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
from datetime import datetime

# Replace YOUR_API_KEY with your own Alpha Vantage API key
api_key = "YOUR_API_KEY"

# Specify the base and quote currencies
base_currency = "USD"
quote_currency = "KES"

# Define the API endpoint URL and parameters
url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={base_currency}&to_symbol={quote_currency}&apikey={api_key}"

# Make a request to the API and parse the response JSON data
response = requests.get(url)
data = response.json()["Time Series FX (Daily)"]

# Convert the response data to a pandas DataFrame
df = pd.DataFrame(columns=["date", "open", "high", "low", "close"])
for date, values in data.items():
    df = df.append({
        "date": datetime.strptime(date, "%Y-%m-%d").date(),
        "open": float(values["1. open"]),
        "high": float(values["2. high"]),
        "low": float(values["3. low"]),
        "close": float(values["4. close"])
    }, ignore_index=True)

# Plot a candlestick chart using Matplotlib
fig, ax = plt.subplots()
ax.xaxis_date()

# Set the x-axis date format
date_fmt = mdates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(date_fmt)

# Plot the candlestick chart
candlestick_ohlc(ax, df.values, width=0.6)

# Set the chart title and axis labels
plt.title(f"{base_currency}/{quote_currency} Forex Rates")
plt.xlabel("Date")
plt.ylabel("Price")

# Show the chart
plt.show()
