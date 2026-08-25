import pandas as pd
import logging
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

def load_to_postgres(df: pd.DataFrame, table_name: str =  "raw_orders"):
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "5432")
    dbname = os.getenv("DB_NAME")

    logging.info(f"Connecting to host={host} port={port} db={dbname} user={user}")

    url = URL.create(
        drivername="postgresql+psycopg2",
        username=user,
        password=password,
        host=host,
        port=int(port),
        database=dbname,
    )
    engine = create_engine(url)

    try:
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        logging.info(f"Load completed: {len(df)} rows loaded into '{table_name}'")
    except Exception as e:
        logging.error(f"Error loading data into PostgreSQL: {e}")
        raise