# etl_config.py 
# This file contains the configuration for the ETL process, including API details and database connection settings.
# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}


# etl/etl_config.py
from dotenv import load_dotenv
import os
from pathlib import Path
import logging # Add this

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # Add this

load_dotenv(dotenv_path='/opt/airflow/.env')

API_KEY = os.getenv("API_KEY")
DB_PASSWORD_VAL = os.getenv("DB_PASSWORD") # Capture the value
logging.info(f"DB_PASSWORD loaded in etl_config.py: '{DB_PASSWORD_VAL}' (length: {len(DB_PASSWORD_VAL) if DB_PASSWORD_VAL else 0})") # Log it
logging.info(f"API_KEY loaded in etl_config.py: '{API_KEY}'") # Confirm API key


DB_CONFIG = {
    "host": "db",
    "port": "5432",
    "user": "postgres",
    "password": DB_PASSWORD_VAL, # Use the captured value
    "dbname": "weather_db"
}

CITIES = ["London", "New York", "Abuja"]
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"