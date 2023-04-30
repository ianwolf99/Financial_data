
import requests
import pandas as pd
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpl_dates

# Set the API endpoint and parameters
url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'kes',
    'ids': 'bitcoin, ethereum, usd-coin',
    'order': 'market_cap_desc',
    'per_page': '100',
    'page': '1',
    'sparkline': 'false',
    'price_change_percentage': '1h,24h,7d'
}

# Retrieve data from API and create pandas dataframe
response = requests.get(url, params=params)
data = response.json()
df = pd.DataFrame(data)

# Clean the data
df = df.drop(['id', 'image', 'current_price', 'market_cap_rank', 'total_volume', 'high_24h', 'low_24h', 'price_change_24h', 'price_change_percentage_24h', 'market_cap_change_percentage_24h'], axis=1)
df = df.rename(columns={'name': 'Name', 'symbol': 'Symbol', 'market_cap': 'Market Cap', 'price_change_percentage_1h_in_currency': '1h', 'price_change_percentage_24h_in_currency': '24h', 'price_change_percentage_7d_in_currency': '7d'})
df = df.set_index('Symbol')
df['Market Cap'] = df['Market Cap'].astype(float)

# Create a candlestick chart using Matplotlib
plt.style.use('ggplot')
plt.figure(figsize=(12,6))
ax = plt.subplot()

ohlc = df['Market Cap'].resample('1D').ohlc()
ohlc.reset_index(inplace=True)
ohlc['Date'] = ohlc['Date'].map(mpl_dates.date2num)

candlestick_ohlc(ax, ohlc.values, width=0.5, colorup='green', colordown='red', alpha=1)

plt.xlabel('Date')
plt.ylabel('Market Cap (in KES)')
plt.title('Cryptocurrencies and USDC Market Cap in Kenya')
plt.legend(df.index)
plt.xticks(rotation=45)
plt.show()
