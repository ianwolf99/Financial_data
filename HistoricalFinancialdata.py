
import requests
import matplotlib.pyplot as plt

# Enter your Coinbase API credentials
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
API_PASS = 'your_api_passphrase'

# Set API endpoints
URL = 'https://api.pro.coinbase.com'
PRODUCTS_ENDPOINT = '/products'
CANDLES_ENDPOINT = '/products/{}/candles'

# Set parameters
product_id = 'BTC-USD'
granularity = 3600  # 1 hour intervals
num_periods = 24  # 24 hours of data

# Set headers and auth
headers = {
    'Content-Type': 'application/json',
    'CB-ACCESS-KEY': API_KEY,
    'CB-ACCESS-SIGN': '',
    'CB-ACCESS-TIMESTAMP': '',
    'CB-ACCESS-PASSPHRASE': API_PASS
}

# Get the products
response = requests.get(URL + PRODUCTS_ENDPOINT, headers=headers)
products = response.json()

# Get the product ID for USDC
usdc_id = None
for product in products:
    if product['id'] == 'USDC-USD':
        usdc_id = product['id']
        break

# Get the historical data for BTC-USD and USDC-USD
btc_data = requests.get(URL + CANDLES_ENDPOINT.format(product_id),
                         headers=headers,
                         params={'granularity': granularity * 60, 'limit': num_periods}).json()
usdc_data = requests.get(URL + CANDLES_ENDPOINT.format(usdc_id),
                          headers=headers,
                          params={'granularity': granularity * 60, 'limit': num_periods}).json()

# Create lists of timestamps and prices for BTC-USD and USDC-USD
btc_timestamps = [data[0] for data in btc_data]
btc_prices = [data[4] for data in btc_data]
usdc_timestamps = [data[0] for data in usdc_data]
usdc_prices = [data[4] for data in usdc_data]

# Plot the data
fig, ax = plt.subplots(2, sharex=True, figsize=(12, 8))
ax[0].plot(btc_timestamps, btc_prices, label='BTC-USD')
ax[1].plot(usdc_timestamps, usdc_prices, label='USDC-USD')

# Add titles, legends, and labels
fig.suptitle('Bitcoin and USDC Prices', fontsize=20)
ax[0].set_title('BTC-USD', fontsize=16)
ax[1].set_title('USDC-USD', fontsize=16)
ax[1].set_xlabel('Time', fontsize=16)
ax[0].set_ylabel('Price (USD)', fontsize=16)
ax[1].set_ylabel('Price (USD)', fontsize=16)
ax[0].legend(fontsize=14)
ax[1].legend(fontsize=14)

# Show the plot
plt.show()
