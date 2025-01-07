import requests
import matplotlib.pyplot as plt
import pandas as pd

# URL for the Blockchain.com API to fetch market price data
url = "https://api.blockchain.info/charts/market-price?timespan=all&format=json"

# Make the API request
response = requests.get(url)
data = response.json()

# Extract the dates and market prices
dates = [entry['x'] for entry in data['values']]  # Timestamps
prices = [entry['y'] for entry in data['values']]  # Bitcoin prices

# Convert the timestamps to readable dates
dates = pd.to_datetime(dates, unit='s')

# Create a DataFrame
df = pd.DataFrame({'Date': dates, 'Price': prices})

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Price'], label='BTC Price')
plt.title('Pablo-wood Bitcoin Market Price (2009-Present)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate date labels for better visibility
plt.savefig('wood2.jpg')
plt.show()
