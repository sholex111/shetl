# etl_config.py 
# This file contains the configuration for the ETL process, including API details and database connection settings.
# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}


from dotenv import load_dotenv
load_dotenv(dotenv_path="weather_etl_pg/.env")
import os

# If your .env is in a subfolder (e.g., config/.env)
# load_dotenv(dotenv_path="config/.env")

# If your .env is in root folder, just:
load_dotenv()

API_KEY = os.getenv("API_KEY")

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": os.getenv("DB_PASSWORD"),
    "dbname": "weatherdb"
}

CITIES = ["London", "New York", "Abuja"]
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
