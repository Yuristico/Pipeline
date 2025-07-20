from psycopg2.extras import RealDictCursor
import psycopg2
from sqlalchemy import create_engine

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "ventas",
    "user": "postgres",
    "password": "12345678"
}

def get_connection():
    return psycopg2.connect(
        dbname=DB_CONFIG["dbname"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        cursor_factory=RealDictCursor
    )

def get_engine():
    return create_engine(
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    )

