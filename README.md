# SHETL: Simple Hybrid ETL Pipeline

A modular, Python-based ETL solution that integrates data from various sources into PostgreSQL, with support for Docker and Airflow.

---

## Components

### `etl_load_data.py`
- Extracts data from **MS SQL Server**.
- Loads it into **PostgreSQL**.
- Useful for working with **AdventureWorks** database.

### `weather_etl_pg`
- Extracts weather data via API.
- Transforms and loads it into local **PostgreSQL**.
- Upserts data with each run.

### `etl_docker`
- Dockerized ETL process for weather data.
- Automates extraction and loading using **Docker Compose**.
- Supports orchestration with **Apache Airflow**.

---

## 🔧 Process Overview

### 🐘 `etl_load_data.py`

1. Ensure **MS SQL Server** is installed on your PC.
2. Load the **AdventureWorks** sample database into MS SQL.
3. Install and start **PostgreSQL**.
4. Create the `adventureworks` database manually using SQL scripts from `SHETL/sql`.
5. Open terminal and navigate to the project folder:
   ```bash
   cd path/to/project
6. Run the ETL script:
-  python etl_load_data.py

7. Fix any bugs or errors if encountered.


##  weather_etl_pg

This component extracts weather data using a public API, transforms it, and loads it into a PostgreSQL database on your local machine.

---

### Contents

- `run_pipeline.py`: Main script to extract, transform, and load data
- `sql/`: SQL script(s) to create the target database and table
- You can find the script in: `weather_etl_pg/sql/create_weather_table.sql`

### Configure .env

```
Make sure you have a .env file in the weather_etl_pg/ folder with variables like:
API_KEY=your_api_key_here
DB_HOST=localhost
DB_PORT=5432
DB_NAME=weather_db
DB_USER=postgres
DB_PASSWORD=your_password
```

### Run the Pipeline

- In your terminal, navigate to the weather_etl_pg folder:
- cd path/to/weather_etl_pg
- python run_pipeline.py

### What to Expect

- Script will connect to the weather API, pull data for specified locations, clean/transform it, and insert into PostgreSQL.

- If data for a specific city and time already exists, it will upsert (update or insert) instead of duplicating.

### Verifying the Result

- Open pgAdmin.

- Connect to weather_db.

- Open Query Tool and run:


## ETL Docker (Run locally on Windows PC)

Ensure you have installed **Docker Desktop** on your PC and it is running.

### Running the Project

1. Open your terminal and navigate to the appropriate project folder.
2. Run the following Docker Compose commands:

```bash
docker compose up --build -d      # Build images and start containers in detached mode
docker compose logs               # Show logs from all containers
docker compose logs -f            # Stream real-time logs (follow mode)
docker compose down -v            # Stop and remove containers, networks, and volumes
docker compose down               # Stop and remove containers, keep volumes
```

### Additional Useful Commands

```bash
docker compose ps                 # List running containers in the project
docker compose exec <svc> sh     # Open shell in a running service container
docker compose restart <svc>     # Restart specific service
docker compose build              # Build or rebuild services
docker compose pull               # Pull service images
```

---

### Accessing Apache Airflow

Visit: [http://localhost:8081/](http://localhost:8081/)

* Click on the current DAG to examine more details.
* Check logs for any errors that need fixing.

---

### Accessing PGAdmin

Visit: [http://localhost:8080/browser/](http://localhost:8080/browser/)

#### Login Details:

```
Email: admin@example.com
Password: admin
```

(These credentials are defined in your `docker-compose.yml` file.)

#### Steps:

1. In the PGAdmin sidebar, right-click on **Servers**.
2. Choose **Create → Server** (or rename the existing one).
3. Under the **Connection** tab, fill in the following:

```
Host name/address: db
Port: 5432
Username: postgres
Password: <your password from .env>
Database: weather_db
```

Click **Save** or **Connect**.

#### Run a query:

```sql
SELECT * FROM weather_data;
```

> Make sure your `.env` file and `docker-compose.yml` have matching DB credentials.

## Author

### Olusola Fajobi

- For feedback, ideas or collaboration — feel free to connect!
