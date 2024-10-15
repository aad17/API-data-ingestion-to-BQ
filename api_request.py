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
    # Normalize JSON data
    normalised_data = pd.json_normalize(data)

    # Convert JSON to oandas dataframe
    df = pd.DataFrame(normalised_data)

    # Define the CSV file path
    csv_file = 'weather_data.csv'

    # Check if the file exists to determine if the header should be written
    if not os.path.isfile(csv_file):
        df.to_csv(csv_file, index=False)
    else:
        df.to_csv(csv_file, mode='a', header=False, index=False)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
