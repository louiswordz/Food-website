import plotly.graph_objects as go
import requests


def get_historical_data(start_date, end_date):
    url = f"https://api.coindesk.com/v1/bpi/historical/close.json?start={start_date}&end={end_date}"
    response = requests.get(url)
    data = response.json()
    
    
    return data['bpi']

data = get_historical_data('2009', '2025') 
dates = list(data.keys())
price = list(data.values())  

fig = go.Figure(data=[go.Scatter(x=dates, y=price, mode='lines', name='Bitcoin Price')])
name ='pablo-wood'
fig.update_layout(title= f'{name} Bitcoin price', xaxis_title='Date',yaxis_title='(USD)')
fig.show()
print('%s analysis for Bitcoin ATH $%s' %(name, 108,319.87))