
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('financial_data.csv', parse_dates=True, index_col='Date')

# Plot the closing prices
plt.plot(data['Close'], label='Closing Prices')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('Stock Prices')

# Add a legend
plt.legend()

# Show the plot
plt.show()
