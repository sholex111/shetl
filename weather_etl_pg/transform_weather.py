# this module transforms weather data for PostgreSQL storage

def transform_weather_data(df):
    df = df.rename(columns={
        'datetime': 'timestamp',
        'weather_main': 'weather'
    })
    df = df[['city', 'temperature', 'humidity', 'weather', 'timestamp']]
    df['citytime'] = df['city'] + "_" + df['timestamp'].astype(str)
    return df
