import os
import sqlite3
import psycopg

SQLITE_DB = "database/school.db"
POSTGRES_URL = os.environ.get("DATABASE_URL")

if not POSTGRES_URL:
    raise SystemExit("ERROR: DATABASE_URL hin jiru.")

sqlite_conn = sqlite3.connect(SQLITE_DB)
sqlite_conn.row_factory = sqlite3.Row

pg_conn = psycopg.connect(POSTGRES_URL)

print("SQLite source: OK")
print("PostgreSQL connection: OK")

sqlite_conn.close()
pg_conn.close()

print("MIGRATION CONNECTION CHECK: OK")
