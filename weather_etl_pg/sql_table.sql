-- This SQL script creates a table for storing weather data.


DROP TABLE IF EXISTS weather_data;

CREATE TABLE weather_data (
    city TEXT,
    temperature REAL,
    humidity INTEGER,
    weather TEXT,
    timestamp TIMESTAMP,
    citytime TEXT PRIMARY KEY
);
