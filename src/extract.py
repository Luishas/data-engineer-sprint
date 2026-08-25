import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

BASE_DIR = Path(__file__).resolve().parent.parent 

def extract_orders(path: str = None) -> pd.DataFrame:
    if path is None:
        path = BASE_DIR / "data" / "raw" / "olist_orders_dataset.csv"
    try:
        df = pd.read_csv(path)
        logging.info(f"Extraction completed: {len(df)} rows read from {path}")
        return df
    except FileNotFoundError as e:
        logging.error(f"Archivo no encontrado: {e}")
        raise