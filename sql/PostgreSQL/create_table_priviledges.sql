-- Create user only if it doesn't exist
DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'shotech') THEN
      CREATE USER shotech WITH PASSWORD 'passpass';
   END IF;
END
$$;

-- Grant basic access
GRANT CONNECT ON DATABASE "AdventureWorks" TO shotech;
GRANT USAGE ON SCHEMA public TO shotech;
GRANT CREATE ON SCHEMA public TO shotech;

-- Grant DML permissions on existing tables
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO shotech;

-- Ensure future tables also have correct permissions
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO shotech;
