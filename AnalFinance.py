
import pandas as pd
import matplotlib.pyplot as plt

# Read in cryptocurrency data from CSV file
df = pd.read_csv('cryptocurrency_data.csv')

# Group data by month and calculate average price
monthly_avg = df.groupby(pd.Grouper(key='date', freq='M')).mean()

# Bar chart of monthly average prices
plt.figure(figsize=(12, 6))
plt.bar(monthly_avg.index, monthly_avg['price'])
plt.title('Monthly Average Cryptocurrency Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()

# Scatter plot of price vs. market cap
plt.figure(figsize=(8, 8))
plt.scatter(df['market_cap'], df['price'])
plt.title('Cryptocurrency Price vs. Market Cap')
plt.xlabel('Market Cap (USD)')
plt.ylabel('Price (USD)')
plt.show()

# Candlestick chart of daily prices
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

# Convert date column to matplotlib dates
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].apply(mdates.date2num)

# Select data for candlestick chart
candle_data = df[['date', 'open', 'high', 'low', 'close']]

# Create candlestick chart
fig, ax = plt.subplots(figsize=(12, 6))
candlestick_ohlc(ax, candle_data.values, width=0.6, colorup='g', colordown='r')
ax.xaxis_date()
plt.title('Daily Cryptocurrency Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()
