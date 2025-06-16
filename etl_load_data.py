#import needed libraries
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
import pyodbc
from dotenv import load_dotenv
import os


load_dotenv()  # Load environment variables from .env file

#set passwordand other var
pwd = os.environ['SQPASS']  # Ensure you have set this environment variable
uid = os.environ['SQID']  # Ensure you have set this environment variable


#sql db details
driver = "ODBC Driver 17 for SQL Server"
server = "SHOLEX111"
database = "AdventureWorksDW2022"


def extract():
    src_conn = None  # Initialize to avoid UnboundLocalError
    try:
        # Connect to SQL Server (ensure instance name is correct, using double backslashes)
        src_conn = pyodbc.connect(
            f'DRIVER={driver};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={uid};'
            f'PWD={pwd}'
        )
        print("✅ Connected to SQL Server successfully.")

        # Create cursor and fetch table names
        src_cursor = src_conn.cursor()
        src_cursor.execute("""
            SELECT t.name AS table_name
            FROM sys.tables t
            WHERE t.name IN (
                'DimProduct',
                'DimProductSubcategory'               
            )
        """)
        src_tables = src_cursor.fetchall()

        # For each table, extract the data and call the load function
        for tbl in src_tables:
            table_name = tbl[0]
            print(f"📦 Extracting data from table: {table_name}")
            df = pd.read_sql_query(f"SELECT * FROM {table_name}", src_conn)
            load(df, table_name)

    except Exception as e:
        print("❌ Data extract error:", str(e))

    finally:
        # Close connection only if it was successfully created
        if src_conn:
            src_conn.close()
            print("🔌 SQL Server connection closed.")


#load data to postgres
def load(df, tbl):
    try:
        rows_imported = 0
        #engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/adventureworks')
        engine = create_engine(f'postgresql+psycopg2://{uid}:{pwd}@localhost:5432/AdventureWorks')
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # save df to postgres
        with engine.connect() as connection: # Get a connection from the engine using a context manager
            df.to_sql(f'stg_{tbl}', connection, if_exists='replace', index=False, chunksize=100000)
        rows_imported += len(df)
        # add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))

try:
    #call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))
