
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests
import json

# Fetching data from API
url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-01-01&end=2021-12-31'
response = requests.get(url)
data = json.loads(response.text)['bpi']

# Converting data to pandas DataFrame
df = pd.DataFrame(list(data.items()), columns=['date', 'price'])
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.sort_index(inplace=True)

# Plotting data
fig, ax = plt.subplots(figsize=(12, 8))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.plot(df.index, df['price'])
plt.title('Bitcoin Historical Prices (2021)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()
