import matplotlib.pyplot as plt
import pandas_datareader as pdr

# Load financial data
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'
df = pdr.get_data_yahoo(ticker, start_date, end_date)

# Calculate moving averages
sma_20 = df['Adj Close'].rolling(window=20).mean()
sma_50 = df['Adj Close'].rolling(window=50).mean()

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Adj Close'], label=ticker)
plt.plot(sma_20.index, sma_20, label='20 day moving average')
plt.plot(sma_50.index, sma_50, label='50 day moving average')

# Set the plot title, x-label, and y-label
plt.title(f'{ticker} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')

# Add the legend and show the plot
plt.legend()
plt.show()
