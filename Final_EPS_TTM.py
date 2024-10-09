import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

# Read the CSV file into a DataFrame
df = pd.read_csv('EPS.csv')

# Set the first column as the index (assuming it contains date information)
df.index = pd.to_datetime(df.iloc[:, 0])

# Define the start and end dates for the quarter frequency
start_date = '2019-09-30'
end_date = '2024-06-30'

# Create a date range at quarterly frequency
date_index = pd.date_range(start=start_date, end=end_date, freq='Q')

eps_values = []
# Resample the DataFrame to quarterly frequency, filling missing values
df = df.resample('Q').asfreq()

# Filter out rows that are not the end of a quarter
df = df[df.index.isin(date_index)]

# Drop the column by index before calculating the rolling sum
df = df.rolling(window=4).sum()
df = df.resample('D').asfreq()
df = df.ffill()
df = df.rename(index={pd.Timestamp('2024-06-30'): pd.Timestamp('2024-07-01')})
df.index.name = 'Date'

# Save the resampled DataFrame to a new CSV file
df.to_csv("resample.csv")

# Concatenating the DataFrame along the columns (if needed)
df = pd.concat([df], axis=1)

# print(df)
