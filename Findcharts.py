
import requests
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# define cryptocurrency and currency symbols
cryptocurrency = 'BTC'
currency = 'USD'

# define API URL
url = f'https://api.coingecko.com/api/v3/coins/{cryptocurrency}/market_chart?vs_currency={currency}&days=7'

# make API request and retrieve data
response = requests.get(url)
data = response.json()

# parse data into a pandas dataframe
df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)

# create a candlestick chart
mpf.plot(df, type='candle', volume=True, style='charles', title=f'{cryptocurrency} Price')

# create a line chart
plt.plot(df.index, df['price'])
plt.title(f'{cryptocurrency} Price')
plt.xlabel('Time')
plt.ylabel(f'Price ({currency})')
plt.show()
