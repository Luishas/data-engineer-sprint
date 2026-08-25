import pandas as pd
import logging
from pathlib import Path
from typing import Optional, Union

logging.basicConfig(level=logging.INFO)

BASE_DIR = Path(__file__).resolve().parent.parent 

def extract_csv(filename: str, path: Optional[Union[str, Path]] = None) -> pd.DataFrame:
    if path is None:
        path = BASE_DIR / "data" / "raw" / filename
    try:
        df = pd.read_csv(path)
        logging.info(f"Extraction completed: {len(df)} rows read from {filename}")
        return df
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise