
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Get cryptocurrency data
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
params = {'vs_currency': 'kes', 'days': '30'}
response = requests.get(url, params=params)
data = response.json()

# Get USDC data
url_usdc = 'https://api.coingecko.com/api/v3/coins/tether/market_chart'
params_usdc = {'vs_currency': 'kes', 'days': '30'}
response_usdc = requests.get(url_usdc, params=params_usdc)
data_usdc = response_usdc.json()

# Extract data
btc_prices = data['prices']
usdc_prices = data_usdc['prices']
dates = [datetime.fromtimestamp(x[0]/1000.0) for x in btc_prices]

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Plot BTC prices
ax1.plot(dates, [x[1] for x in btc_prices], label='BTC')
ax1.set_ylabel('Price (KES)')
ax1.legend()

# Plot USDC prices
ax2.plot(dates, [x[1] for x in usdc_prices], label='USDC')
ax2.set_xlabel('Date')
ax2.set_ylabel('Price (KES)')
ax2.legend()

# Show plot
plt.show()

