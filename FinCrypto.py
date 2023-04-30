
import matplotlib.pyplot as plt
import pandas as pd
import requests

# Set the API endpoint URL and cryptocurrency symbol
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"
symbol = "BTC"

# Call the API and store the data
response = requests.get(url)
data = response.json()

# Extract the prices from the API data
prices = [x[1] for x in data["prices"]]
timestamps = [pd.Timestamp(x[0], unit='ms') for x in data["prices"]]

# Create a pandas dataframe with the prices and timestamps
df = pd.DataFrame({'price': prices}, index=timestamps)

# Create a line chart using matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df.price)

# Set the chart title and axis labels
ax.set_title(f"{symbol} Price Chart (last 30 days)")
ax.set_xlabel("Date")
ax.set_ylabel(f"{symbol} Price (USD)")

# Format the x-axis to display dates
date_format = mpl_dates.DateFormatter('%m-%d-%Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

# Display the chart
plt.show()
