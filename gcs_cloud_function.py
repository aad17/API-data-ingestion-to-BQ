import pandas as pd
from transform import transform
from config import proj, dataset, table

def process_csv(cloud_event):
  data = cloud_event.data
  bucket = data["bucket"]
  file_name = data["name"]

  df = pd.read_csv(f'gs://{bucket}/{file_name}')
  df_transformed = pd.DataFrame.from_records(transform(df))

  df_transformed.to_gbq(f'{dataset}.{table}',
                        project_id=f'{proj}',
                        if_exists='append',
                        location='eu')