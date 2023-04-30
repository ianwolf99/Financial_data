import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Define API endpoint and parameters
url = "https://api.coincap.io/v2/assets"
params = {
    "limit": "100"
}

# Make API request and get data
response = requests.get(url, params=params)
data = json.loads(response.content.decode('utf-8'))

# Create a pandas dataframe with relevant data
df = pd.DataFrame(data['data'], columns=['name', 'symbol', 'priceUsd', 'changePercent24Hr'])
df['priceUsd'] = pd.to_numeric(df['priceUsd'])
df['changePercent24Hr'] = pd.to_numeric(df['changePercent24Hr'])
df = df.set_index('symbol')

# Create a bar chart of the top 10 cryptocurrencies by market cap
df_top10 = df.sort_values('priceUsd', ascending=False)[:10]
df_top10.plot(kind='bar', y='priceUsd', legend=None)
plt.title('Top 10 Cryptocurrencies by Market Cap')
plt.xlabel('Symbol')
plt.ylabel('Price (USD)')
plt.show()

# Create a scatter plot of all cryptocurrencies by 24-hour price change and price
plt.scatter(df['changePercent24Hr'], df['priceUsd'])
plt.title('Cryptocurrencies by 24-Hour Price Change and Price')
plt.xlabel('24-Hour Price Change (%)')
plt.ylabel('Price (USD)')
plt.show()

# Create a candlestick chart of Bitcoin prices over the past week
url = "https://api.coincap.io/v2/assets/bitcoin/history"
params = {
    "interval": "d1",
    "start": (datetime.now() - pd.DateOffset(days=7)).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
    "end": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
}
response = requests.get(url, params=params)
data = json.loads(response.content.decode('utf-8'))
df_btc = pd.DataFrame(data['data'], columns=['time', 'open', 'high', 'low', 'close', 'volume'])
df_btc['time'] = pd.to_datetime(df_btc['time'])
df_btc = df_btc.set_index('time')
df_btc = df_btc[['open', 'high', 'low', 'close']]
df_btc.plot(kind='candle', legend=None)
plt.title('Bitcoin Prices over the Past Week')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()
