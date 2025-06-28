#extract_weather.py
# this script extracts weather data from the OpenWeatherMap API for a list of cities
# and transforms it into a long format suitable for analysis.


import requests
import pandas as pd
import logging # Import logging
from .etl_config import API_KEY, BASE_URL, CITIES

# Configure basic logging (for development/debugging)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_weather_data():
    forecast_data = []

    for city in CITIES:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric' # To get temperature in Celsius
        }
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric" # For easier logging of full URL
        logging.info(f"Attempting to fetch data for {city}. URL: {url}")

        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status() # This will raise an HTTPError for bad responses (4xx or 5xx)

            data = response.json()
            logging.info(f"Successfully fetched data for {city}. Response keys: {data.keys()}")

            if 'list' in data:
                logging.info(f"Found 'list' in response for {city}. Processing {len(data['list'])} entries.")
                for entry in data['list']:
                    # Validate keys exist before appending, especially for nested dictionaries
                    # Defensive programming here
                    if all(k in entry for k in ['dt_txt', 'main', 'weather', 'wind']) and \
                       all(k in entry['main'] for k in ['temp', 'feels_like', 'humidity']) and \
                       len(entry['weather']) > 0 and 'main' in entry['weather'][0] and \
                       'speed' in entry['wind']:
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
                        logging.warning(f"Skipping malformed entry for {city}: {entry}. Missing expected keys.")
            else:
                logging.warning(f"No 'list' key found in API response for {city}. Full response: {data}")

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error for {city}: {http_err} - Response: {response.text}")
        except requests.exceptions.ConnectionError as conn_err:
            logging.error(f"Connection error for {city}: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            logging.error(f"Timeout error for {city}: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            logging.error(f"An error occurred during request for {city}: {req_err}")
        except KeyError as k_err:
            logging.error(f"KeyError encountered for {city}: Missing key in API response - {k_err}. Response snippet: {data.get('list', [])[:1]}...") # Log problematic part
        except Exception as e:
            logging.error(f"An unexpected error occurred for {city}: {e}")

    df = pd.DataFrame(forecast_data)

    if df.empty:
        logging.error("DataFrame is EMPTY after extraction. Check API key and network connectivity.")
    else:
        logging.info(f"DataFrame successfully created. Columns: {df.columns.tolist()}")
        logging.info(f"First 5 rows of extracted DataFrame:\n{df.head().to_string()}")

    return df