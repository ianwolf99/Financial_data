

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

# Define the API endpoint and parameters
url = "https://www.freeforexapi.com/api/live"
parameters = {"pairs": "USDZAR,USDJPY,USDGBP,USDEUR,USDKES"}

# Send a GET request to the API endpoint with the specified parameters
response = requests.get(url, params=parameters)

# Parse the response data as a JSON object
data = json.loads(response.text)

# Create a Pandas dataframe from the parsed JSON data
df = pd.DataFrame(data["rates"]).transpose()

# Convert the 'timestamp' column to a datetime object and set it as the index
df.index = pd.to_datetime(df["timestamp"])
df = df.drop(["timestamp"], axis=1)

# Create a new column for the USD/KES exchange rate
df["USD/KES"] = 1/df["USD/KES"]

# Resample the data to daily frequency and fill any missing values with the previous day's value
df = df.resample("D").ffill()

# Define the figure and subplot
fig, ax = plt.subplots(figsize=(12, 6))

# Create a candlestick chart using the 'plot_date' function from the 'mpl_finance' library
ohlc = df[["USDJPY", "USDGBP", "USDEUR", "USDZAR", "USD/KES"]].copy()
ohlc["date"] = mdates.date2num(ohlc.index.to_pydatetime())
candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='g', colordown='r', alpha=0.8)

# Format the x-axis as dates
date_format = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

# Set the chart title and labels
ax.set_title("Forex Exchange Rates", fontsize=16)
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Exchange Rate", fontsize=12)
plt.legend(["USD/JPY", "USD/GBP", "USD/EUR", "USD/ZAR", "USD/KES"])

# Display the chart
plt.show()
