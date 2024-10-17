import os
import pandas as pd
import datetime


df = pd.read_csv('weather_data.csv')
def transform(df):
    weather_dict = eval(df['weather'][0][1:-1])
    df2 = df[['main.humidity', 'main.temp', 'wind.speed', 'dt']]
    df2['description'] = pd.Series(weather_dict)['description']
    df2['main.humidity'] = df2['main.humidity'].astype('float')
    df2 = get_date_time(df2)
    df2.rename(columns={'main.humidity': 'humidity', 'main.temp': 'temperature', 'wind.speed': 'wind_speed'}, inplace=True)
    return df2


def get_date_time(df2):
    dt_date = []
    dt_time = []
    for x in range(len(df2)):
        date_time_str = str(datetime.datetime.fromtimestamp(int(df2['dt'].iloc[x]))).split(' ')
        date_str = date_time_str[0]
        time_str = date_time_str[1]
        dt_date.append(date_str)
        dt_time.append(time_str)
    dt_date = pd.to_datetime(pd.Series(dt_date))
    dt_time = pd.to_datetime(pd.Series(dt_time))
    df2['date'] = dt_date
    df2['time'] = dt_time
    return df2


def save_csv(df):
    csv_file = 'weather_data_transformed.csv'

    if not os.path.isfile(csv_file):
        df.to_csv(csv_file, index=False)
    else:
        df.to_csv(csv_file, mode='a', header=False, index=False)

df2 = transform(df)
save_csv(df2)