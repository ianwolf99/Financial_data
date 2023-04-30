

import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
df = pd.read_csv('crypto_data.csv')

# Line chart
plt.plot(df['Date'], df['BTC'], label='BTC')
plt.plot(df['Date'], df['ETH'], label='ETH')
plt.plot(df['Date'], df['LTC'], label='LTC')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Cryptocurrency Prices')
plt.legend()
plt.show()

# Bar chart
plt.bar(df['Date'], df['Volume'])
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Cryptocurrency Trading Volume')
plt.show()

# Scatter plot
plt.scatter(df['BTC'], df['ETH'])
plt.xlabel('BTC Price')
plt.ylabel('ETH Price')
plt.title('BTC vs ETH Price')
plt.show()
