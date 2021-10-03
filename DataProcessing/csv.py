#!pip install pandas
#!pip install requests

import pandas as pd

url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
df = pd.read_csv(url)

#Add column names
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

# To select the first row
df.loc[0]

# To select the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name" ]

# To select the 0th,1st and 2nd row of "First Name" column only
df.iloc[[0,1,2], 0]

# Add 10 to each element
df = df.transform(func = lambda x : x + 10)

# Find sqrt
result = df.transform(func = ['sqrt'])
