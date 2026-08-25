import pandas as pd
import logging

def transform_generic(df: pd.DataFrame, key_column:str) -> pd.DataFrame:
    df = df.copy()

    date_cols  = [c for c in df.columns if "date" in  c or "timestamp" in c]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    if key_column in df.columns:
        nulls_id = df[key_column].isnull().sum()
        if nulls_id > 0:
            logging.warning(f"{nulls_id} rows without {key_column} - eliminated")
            df = df.dropna(subset=[key_column])

        duplicates = df.duplicated(subset=[key_column]).sum()
        if duplicates > 0:
            logging.warning(f"{duplicates} {key_column} duplicated found - eliminated")
            df = df.drop_duplicates(subset=[key_column])

    logging.info(f"Transformation completed: {len(df)} final rows")
    return df