from google.cloud import storage
import pandas as pd
from transform import transform

df = pd.read_csv('weather_data.csv')
df = transform(df)
client = storage.client()
bucket = client.get_bucket('gs://ad_weather_transformation_proj')
bucket.blob('weather_transform/csv').upload_from_string(df.to_csv(), 'text/csv')