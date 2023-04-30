
import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV file
data = pd.read_csv('stock_data.csv', index_col=0)

# Set up the figure and axes
fig, ax = plt.subplots()

# Create a line chart of the stock prices
ax.plot(data.index, data['price'], label='Stock Price')

# Create a bar chart of the trading volume
ax2 = ax.twinx()
ax2.bar(data.index, data['volume'], color='gray', alpha=0.5, width=0.2, label='Volume')

# Add titles and labels to the chart
ax.set_title('Stock Price and Trading Volume')
ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax2.set_ylabel('Volume')

# Add a legend to the chart
ax.legend(loc='upper left')
ax2.legend(loc='upper right')

# Display the chart
plt.show()
