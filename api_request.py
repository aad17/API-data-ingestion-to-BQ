import os
import requests
import pandas as pd
from dotenv import load_dotenv
from config import BASE_URI, LAT, LON

load_dotenv()
api_key = os.getenv('API_KEY')
api_url = f'{BASE_URI}lat={LAT}&lon={LON}&appid={api_key}'
try:
    response = requests.get(api_url, verify=False)
    response.raise_for_status()  # Check if the request was successful
    data = response.json()  # Parse the JSON response
    print(data)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")

normalised_data = pd.json_normalize(data)
df = pd.DataFrame(normalised_data)
print(df)
df.to_csv('weather_data.csv', index=False)
print("Data has been stored in weather_data.csv")