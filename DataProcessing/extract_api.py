#!pip install pandas
#!pip install requests

import requests
import pandas as pd

# Write your code here
url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=xxx" 
html = requests.get(url)
a = html.json()

# Turn the data into a dataframe
df = pd.DataFrame(a)
df = df.rename(columns={'rates': 'Rates'})


# Drop unnescessary columns
df = df.drop(['success', 'timestamp', 'base', 'date'], 1)

# Save the Dataframe
df.to_csv('exchange_rates_1.csv')
