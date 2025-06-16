# from sqlalchemy import create_engine
# import pandas as pd

# engine = create_engine("postgresql+psycopg2://shotech:passpass@localhost:5432/adventureworks")
# print("✅ Engine created:", engine)
# df = pd.DataFrame({'test': [1, 2, 3]})
# df.to_sql('test_table', engine, if_exists='replace', index=False)
# print("Test table uploaded successfully")



# from sqlalchemy import create_engine

# engine = create_engine("postgresql+psycopg2://shotech:passpass@localhost:5432/adventureworks")
# print("✅ Engine created:", engine)


# df.to_sql('test_table', engine, if_exists='replace', index=False)




# from sqlalchemy import create_engine
# import pandas as pd

# # Local PostgreSQL connection using SQLAlchemy + psycopg2
# engine = create_engine('postgresql+psycopg2://shotech:passpass@localhost:5432/adventureworks')
# print("✅ Engine created:", engine)

# # Create test DataFrame
# df = pd.DataFrame({
#     'product_id': [101, 102, 103],
#     'product_name': ['Chair', 'Table', 'Lamp']
# })

# # Load to PostgreSQL
# df.to_sql('test_table', engine, if_exists='replace', index=False)
# print("✅ Test data uploaded to 'test_table' successfully")




import pandas as pd
from sqlalchemy import create_engine, text

# Assume df is your DataFrame (example: creating a dummy DataFrame)
data = {'col1': [1, 2], 'col2': ['A', 'B']}
df = pd.DataFrame(data)

# Database connection string
db_connection_str = 'postgresql+psycopg2://shotech:passpass@localhost:5432/AdventureWorks'

engine = create_engine(db_connection_str) # Create the engine
print("✅ Engine created:", engine)

try:
    with engine.connect() as connection: # Get a connection from the engine using a context manager
        df.to_sql('test_table', connection.connection, if_exists='replace', index=False) # Pass the connection to to_sql
    print("✅ DataFrame successfully written to 'test_table'.")

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    pass # The connection is automatically closed when exiting the 'with' block.
         # If you were managing connections manually, you'd explicitly close it here.
