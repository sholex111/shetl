# this script runs the ETL pipeline for weather data extraction, transformation, and loading into PostgreSQL.

from extract_weather import extract_weather_data
from transform_weather import transform_weather_data
#from load_to_postgres import load_to_postgres
from upsert_to_postgres import upsert_to_postgres
import logging
import os

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO, format='%(asctime)s %(message)s')

def run_etl():
    logging.info("Starting ETL process...")
    raw_df = extract_weather_data()
    logging.info(f"Extracted {len(raw_df)} records.")
    transformed_df = transform_weather_data(raw_df)
    #load_to_postgres(transformed_df)
    upsert_to_postgres(transformed_df)
    logging.info("loading to postgress complete.")
    print("ETL process completed successfully.")

if __name__ == "__main__":
    run_etl()
