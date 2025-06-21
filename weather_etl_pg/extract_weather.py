# this script extracts weather data from the OpenWeatherMap API for a list of cities
# and transforms it into a long format suitable for analysis.


import requests
import pandas as pd
from etl_config import API_KEY, BASE_URL, CITIES

def extract_weather_data():
    forecast_data = []

    for city in CITIES:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            for entry in data['list']:
                forecast_data.append({
                    'city': city,
                    'datetime': entry['dt_txt'],
                    'temperature': entry['main']['temp'],
                    'feels_like': entry['main']['feels_like'],
                    'humidity': entry['main']['humidity'],
                    'weather_main': entry['weather'][0]['main'],
                    'weather_description': entry['weather'][0]['description'],
                    'wind_speed': entry['wind']['speed']
                })
        else:
            print(f"Failed to fetch data for {city}: {response.status_code}")

    return pd.DataFrame(forecast_data)
