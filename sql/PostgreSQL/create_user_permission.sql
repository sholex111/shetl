-- This script creates a user named 'shotech' and grants it permissions on the AdventureWorks database.
--create shotech user
CREATE USER shotech WITH PASSWORD 'passpass';
--grant connect
GRANT CONNECT ON DATABASE "AdventureWorks" TO shotech;
--grant table permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO shotech;