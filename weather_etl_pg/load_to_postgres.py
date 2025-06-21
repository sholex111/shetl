# this script loads data into PostgreSQL using SQLAlchemy
# and psycopg2 for database connection.

from sqlalchemy import create_engine
from etl_config import DB_CONFIG

def load_to_postgres(df):
    db_url = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
             f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"

    engine = create_engine(db_url)
    df.to_sql("weather_data", engine, if_exists="append", index=False)
