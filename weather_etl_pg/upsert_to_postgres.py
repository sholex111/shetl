# This code is part of a weather ETL pipeline that upserts data into a PostgreSQL database.
# This script defines a function to upsert weather data into a PostgreSQL database using SQLAlchemy.

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.dialects.postgresql import insert
from etl_config import DB_CONFIG

def upsert_to_postgres(df):
    db_url = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
             f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    engine = create_engine(db_url)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    weather_table = Table('weather_data', metadata, autoload_with=engine)

    with engine.begin() as conn:
        for _, row in df.iterrows():
            stmt = insert(weather_table).values(**row.to_dict())
            stmt = stmt.on_conflict_do_update(
                index_elements=['citytime'],
                set_={
                    "temperature": stmt.excluded.temperature,
                    "humidity": stmt.excluded.humidity,
                    "weather": stmt.excluded.weather,
                    "timestamp": stmt.excluded.timestamp,
                    "city": stmt.excluded.city,
                }
            )
            conn.execute(stmt)
