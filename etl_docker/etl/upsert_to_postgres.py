#upsert_to_postgres.py


from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, Integer, DateTime, insert
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.exc import ProgrammingError
from sqlalchemy import inspect
from .etl_config import DB_CONFIG


def upsert_to_postgres(df):
    db_url = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
             f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    engine = create_engine(db_url)
    metadata = MetaData()

    table_name = "weather_data"

    # Step 1: Check if table exists
    inspector = inspect(engine)
    if not inspector.has_table(table_name):
        print(f"Table '{table_name}' does not exist. Creating it...")

        # Define the schema with a UNIQUE constraint on 'citytime'
        weather_table = Table(
            table_name,
            metadata,
            Column("city", String, nullable=False),
            Column("timestamp", DateTime, nullable=False),
            Column("temperature", Float),
            Column("humidity", Integer),
            Column("weather", String),
            Column("citytime", String, unique=True),  # Unique index here
        )

        metadata.create_all(engine)  # Create the table in DB
        print(f"Table '{table_name}' created successfully with unique constraint on 'citytime'.")

    # Step 2: Reflect table and begin upsert
    metadata.reflect(bind=engine)
    weather_table = Table(table_name, metadata, autoload_with=engine)

    with engine.begin() as conn:
        for _, row in df.iterrows():
            stmt = pg_insert(weather_table).values(**row.to_dict())
            stmt = stmt.on_conflict_do_update(
                index_elements=["citytime"],
                set_={
                    "temperature": stmt.excluded.temperature,
                    "humidity": stmt.excluded.humidity,
                    "weather": stmt.excluded.weather,
                    "timestamp": stmt.excluded.timestamp,
                    "city": stmt.excluded.city,
                }
            )
            conn.execute(stmt)
