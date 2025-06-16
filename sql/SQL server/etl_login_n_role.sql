-- Create a login and user for ETL operations in SQL Server
-- This script creates a login named 'shotech' and grants it permissions on the AdventureWorksDW2022 database.

USE [master]
GO
CREATE LOGIN [shotech] WITH PASSWORD=N'passpass', DEFAULT_DATABASE=[AdventureWorksDW2022], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
USE [AdventureWorksDW2022]
GO
CREATE USER [shotech] FOR LOGIN [shotech]
GO
USE [AdventureWorksDW2022]
GO
ALTER ROLE [db_datareader] ADD MEMBER [shotech]
GO
use [master]
GO
GRANT CONNECT SQL TO [shotech]
GO