import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
import time
import random 
import csv

def random_delay():
    time.sleep(random.uniform(0, 8))

# Send a GET request to the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the components
table = soup.find("table", class_="wikitable sortable")

# Find all the rows in the table (excluding the header row)
rows = table.find_all("tr")[1:504]
# Constituents of S&P500
constituents=[]
industry_list=[]

# Extract the company symbol from each row
for row in rows:
    columns = row.find_all("td")
    symbol = columns[0].text.strip().replace(".", "-")
    industry = columns[2].text.strip()
    constituents.append(symbol)
    industry_list.append(industry)

#print(constituents)
df1 = pd.read_csv('Final_EPS_TTM.csv')
#price=yf.download(constituents,period="max")["Adj Close"]
df1.columns = df1.columns.str.replace(".", "-")
pricedf = pd.read_csv("pricedf.csv")
pricedf.columns = pricedf.columns.str.replace(".", "-")
pricedf['Date'] = pd.to_datetime(pricedf['Date'])
pricedf['Date'] = pricedf['Date'].dt.strftime('%Y-%m-%d')
# Merge the EPS and price DataFrames based on dates and ticker symbols
df_merged = pd.merge(pricedf, df1, on='Date')

# Calculate the Price-to-EPS ratio for all tickers in a vectorized way
price_cols = [f'{ticker}_x' for ticker in constituents]
eps_cols = [f'{ticker}_y' for ticker in constituents]

for x, y in zip(price_cols, eps_cols):
    ratio_column_name = f'PE_Ratio_{x.split("_")[0]}'  # Extracting the ticker symbol from x
    df_merged[ratio_column_name] = df_merged[x] / df_merged[y]
    print(df_merged[ratio_column_name])
df_merged.to_csv("PE_Final.csv")

# new_cols = [f'PE_Ratio_{ticker}' for ticker in constituents]
# new_data = (df_merged[price_cols])/(df_merged[eps_cols])
# df_merged = pd.concat([df_merged, pd.DataFrame(new_data, columns=new_cols)], axis=1)

