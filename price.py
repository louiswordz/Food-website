import requests
import plotly.graph_objects as go
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

fig = go.Figure(data=[go.Scatter(x=df.Date, y=df.Price, mode='lines', name='Bitcoin Price')])
name ='pablo-wood'
fig.update_layout(title= f'{name} Bitcoin Market Price (2009-Present)', xaxis_title='Date',yaxis_title='(USD)')
fig.show()