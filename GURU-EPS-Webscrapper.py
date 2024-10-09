import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
import time
import random 
import csv
import re
cookies = {
    'DSID': 'AB_BQxkcXjqXL-T45ixgU0iOLau8YrQ-mTVaB-w0SAjkWxSLijLvd9cwVlrCN84BjJ9WorKAZFfr7x7mV60_IJyOJ32LIMV57XKGp4-tHxTAgswBeJNKSIub1RPEjU-RTolVJ_Vc_q2lIW87ntt7vHz5ZtUZe0hLelVo5bXqxYDFFj48FnC-sTIoTe3baqI49hoOb6B1X3VkQFh721VVQ34I1d2_hNQvnzcFpvh9NMVbJSJOp558LaO3bDl0QORh63cXOVvjONYLk5nCrfKhr9qR7FSutBG-RLKmGoHSCe2vaqSCmNKpWIQ',
    'PHPSESSID': 'rpsnmuilf5t9ssslh5her364h0',
    'id': 'OPT_OUT',
    'password_grant_custom.client': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjZlZDFmY2JmNWNkYzQ1OTEyODEwOTEzMWRmNzVhMjgwMjExZjEzNmI0M2VkOGJhMjU5YzJlZjM0YmEwMDRmM2ZjNGVjYjg0OTUxMWU4NzA4In0.eyJhdWQiOiIyIiwianRpIjoiNmVkMWZjYmY1Y2RjNDU5MTI4MTA5MTMxZGY3NWEyODAyMTFmMTM2YjQzZWQ4YmEyNTljMmVmMzRiYTAwNGYzZmM0ZWNiODQ5NTExZTg3MDgiLCJpYXQiOjE3MjQ4ODI3MTMsIm5iZiI6MTcyNDg4MjcxMywiZXhwIjoxNzM1MjUwNzEyLCJzdWIiOiIiLCJzY29wZXMiOltdfQ.N7WLvqW-wdjc51bUaM9H9WkmHo7XtmFPYQwdiqeTPvazzeaVyV7D2cz_nmB3iWjkTWxeGzaeOjhYtgBy7vieBp1xqxnJfv0RMATAp55xkL9hQGYKaNOerN3aO5H17h3ni6B8fhHLI3jrLgsB7bWUI1eDTQI5q6JcXnXK3JC-bbQ41RHW6EFJIuoFLMveoq_OPZugo6TIxdKOy1gL9rJaiC49_j-88S_xVqgM-E1gBYKkFdreheyF9uDZ_Gk1Nvh6IhnCoqbgQUNYVHnvFze6j1MahpHsNM-1re4tpHSolkbgsrFiyKuGSqlyZZ3D5ucN3-kfTEyU0MYTy0qspJnM8ibFGg-Uk7c25RDsLgIVkrDe7qtr2K45tTLmRQVlsPPGF3LzH0KFqU7ff2xj3TbvX2EJkHB1b0uK9pvuecHkHtGp0CaWTewHpNEEtkTjUiToUThs_XMVaTbQ0HUNba0c_FqxxL0Iw4TEwpkwk5QuCKH5oN2cQQRVvl5EKof0cSGgCHJSf_zBjOX1aBYVN3eX_wx8TFAmslSvgM5qZNVV-ly-18q-K-WHG4_6rossrcu2b4YqgouGKUaSJURPQlO74byE71Z-4tEKC_fwggVRv6gggWA_0SX8-7b_OAOWq3kOCrza-HVaVFdlrQMHNj9uyf3_T_1wq5aQAk_mie5hUWw',
    'password_grant_custom.client.expires': '1735250712',
    'password_grant_custom.expires': '1730113114',
    'password_grant_custom.refresh_token': 'def502000b91b1c27e4f0d079206ff4533c4d357e5cfd61dcfa3793a766b1fbd8e9f08576d2024c82ac515dde0d912e0b590058321c0f6aa765521718734fdeda5b12bf2a3c76c357d101570a23c93273be8639718b30c57f596a977d207a07ace3c075e4a798feae3861e5df18cd5ee3577f6430b03f3ba0406db9bf24b1d1ee9c8f97e143cc73449a9bb602de335e17bb99e55a0c36d101782bfd45a1ff4dc2a167ad09ea2ab34827d871470463fa8969078478c30d9f6408ad8284d9e2af73321471f2c39d900e2872b27409ec86b8608e3d93553d135142a1e71c476ffc7c7c2744c43bcbc5afb0411ff409ce377d65540ac1af138d4033e6607048a3a69c5a28ea2089027dd09b286e648fbf1dc1164f0b7e0d05af6a0e62055d7620881cf0399b0bae8444e124725cb876209fe69227799e518519bd2a566fbff917fad75b48ffd65e5a856c31a818406f704ca4dbc63008c79fbe60e1f9ff85078b09ba8ef6df982',
    'password_grant_custom.token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjY2NDM3MjBmNjUyOGI3YTJlZGM5NmRmZTI2MTNiNjhhY2U2YjQ3MDgzNGRmMzIwOTM2NWRiZjk0YWY2NWJmYWU3NzBiNWMwMzM3MmI5ZTUxIn0.eyJhdWQiOiIyIiwianRpIjoiNjY0MzcyMGY2NTI4YjdhMmVkYzk2ZGZlMjYxM2I2OGFjZTZiNDcwODM0ZGYzMjA5MzY1ZGJmOTRhZjY1YmZhZTc3MGI1YzAzMzcyYjllNTEiLCJpYXQiOjE3MjQ5MjkxMTQsIm5iZiI6MTcyNDkyOTExNCwiZXhwIjoxNzMwMTEzMTE0LCJzdWIiOiIxMzM2MTIzIiwic2NvcGVzIjpbXX0.SghVy9SMNcBiDpKP_2qwxcjNodwU37p9jWEvDyHvdTGaxMukOp9t4pwzcsl2n_3UONVQ8WLRCGCAZujP6okU8Nftt7rltgM4RHcfRYf9DuQBMORsnTYZaFWvlPGTByoUrkIBQsD_fgYBfQVw9a7yw_a7IWB4pEjgbWsF9UvzuXBs59UZticOSq20z0OlpMPBhh4cZ5aB6KQLRp6lojhU4oyoda525nGe1Pu-IwkV_pu1MJrC6sgOCqjBrO_vdZ0a1BvTKbBep6VL-NyhJgCz9uqUK1z3E01agb_OprId43FmqYCiTVmK97zSO6CgOOhbeOg_icTGPOBUzI9UdZnY7WfScYFVfFQiObwZQkzcQL3NgcIl0q_S-rH9v_Jbdz_W_jgS2gJKmdvLmjK34-1x2Q6ahSvTfoIg70EIi1Ep4SS63pSLag4Y6FVeNG6ppqSwx6QMfUKBd6kOlxbM6ySUWvHlQ6MNbl-4VEk3ICOTkVQQc43VSSGdQxyHWm6QsHwXbn_sbpzFRbAzd2eD_iMQxsc6_9EtaAXTqy4c1DnALC3LtXD7Jrz8fFqvSBfwGg7TWXPqOhXLLMyN6D492hzsEO7DEJpIBNVqjrNRKtTygfhmAJGb50Wvyf6x8-xmRHkl3fqacidE0EmoOruxKCrm1DbIZqWwsOE1QLCwkFILY_U',
    'phorum_session_v5': '1f890b841225f0d8f0a648493e82ff91:1cac532aa60b97dc043781589cba02ad',
    'pwcou': '4',
    'pwcou_flag': '1',
    'stockviewpoint': '/term1.php',
    'strategy': 'password_grant_custom',
    'upgrade_counter': '1',
    'homepage_upgrade_counter_ads': '1724827716',
    'g_state': '{"i_p":1725015504473,"i_l":2}',
    'download_financials_batch': '%2C+MSFT',
    'device_counter': '1724930262',
    'cf_clearance': 'ojpi0l46t8Ftx0Qj3otadi5DeHvg2L8sn8hvLEGKkr8-1725006691-1.2.1.1-oyfGyXhPaKpywYg5FO5p4j5V33sIQ0FjifkQaR84Y01fZPdn0xEv6pK4PUyG3aVOCZZis6hzfAoU0w8xTNi0BWxmcoAUjfgeME4KGGvdQxtAd8Xznyp7kBWoEtOyMAxBJoZWOVKqjXcgGVUQ45RfhpUbc2QZP4y3wKR8R2_OGRxY4b41D1u_laHU4CtvNz9ZrtJYPNWAtnZFHA4uK6.wyTFhB4Is1PUm05NFnadsktju0Vj1JYTvACNrE7N61n6h.fEpdFbFjgV6Veu8sfLzAeg43ENXrFo.h58heCS1S3QGmHB61_0yf8GL7emZwF8hZS5eH4Fei9GKqmy2j0Zoct4hli2wj0.5fAjm2p0KrIuwKAK1EnM5xQrry0x20DrxbUi26VJZ43uUq4Bv9HXbUg',
    'ar_debug': '1',
    '_gid': 'GA1.2.1809594911.1724929067',
    '_gcl_au': '1.1.420169674.1724736968',
    '_ga_T14K4LKYZE': 'GS1.1.1725005858.6.1.1725006727.17.0.0',
    '_ga': 'GA1.1.305382175.1724736962',
    '_clck': '1tooize%7C2%7Cfop%7C0%7C1700'

    # Add more cookies as necessary
}


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
# Constituents of DJI
constituents=[]
industry_list=[]

# Extract the company symbol from each row
for row in rows:
    columns = row.find_all("td")
    symbol = columns[0].text.strip().replace("-", ".")
    industry = columns[2].text.strip()
    constituents.append(symbol)
    industry_list.append(industry)

#print(constituents)

all_pe=pd.DataFrame()

# Specify the path to your text file
file_path = 'proxies.txt'

# Initialize an empty list to store the lines
proxies = []

# Read the text file and categorize the proxies
with open('proxies.txt', 'r') as file:
    for line in file:
        proxies.append(line)

df=[]

for y in constituents:    
    x="https://www.gurufocus.com/term/eps-basic/{}".format(y)
    # Initialize Chrome options
    user_agent = UserAgent()
    proxy = random.choice(proxies)
    random_delay
    response = requests.get(x,headers = {'User-Agent':user_agent.random},proxies={'http':proxy},cookies=cookies)
    random_delay

    # Create a BeautifulSoup object to parse the HTML content

    soup = BeautifulSoup(response.content, "html.parser")
    
    eps_td = soup.find_all("td", string="EPS (Basic)")
    eps_values = []
    if len(eps_td) >= 2:
        # Get the second occurrence of EPS (Basic) td
        eps_td_second = eps_td[1]

        # Extract EPS values following the second EPS (Basic) td
        next_td = eps_td_second.find_next_sibling("td")
        while next_td:
            value = next_td.get_text(strip=True)
            # Check if the value is numeric using regular expression
            if re.match(r'^-?\d+(?:\.\d+)?$', value):
                eps_values.append(value)
            
            # Move to the next <td> element
            next_td = next_td.find_next_sibling("td")
        eps_series = pd.Series(eps_values)
        
       
        print("EPS Values:")
        print(eps_values)
    else:
        eps_series = pd.Series([])  # Set a default value or empty list
        
        print("Second occurrence of EPS (Basic) not found in the HTML content.")
    eps_pd=pd.DataFrame({y:eps_values})
    df.append(eps_pd)
df = pd.concat(df, axis=1)

# Define the starting date and the frequency as quarterly
start_date = '2019-09-30'
end_date = '2024-06-30'

# Create a date range with quarterly frequency
date_index = pd.date_range(start=start_date, end=end_date, freq='Q')

# Set the index of the Series to the date range
df.index = date_index
df = df.resample('D').asfreq()
df = df.ffill()
df.to_csv("EPS.csv")
print(df)