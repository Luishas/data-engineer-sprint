import pandas as pd
import logging

def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    date_cols  = [c for c in df.columns if "date" in  c or "timestamp" in c]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    nulls_id = df["order_id"].isnull().sum()
    if  nulls_id > 0:
        logging.warning(f"{nulls_id}  filas without order_id - eliminated")
        df =  df.dropna(subset=["order_id"])

    duplicates = df.duplicated(subset=["order_id"]).sum()
    if duplicates > 0:
        logging.warning(f"{duplicates} order_id duplicated found - eliminated")
        df = df.drop_duplicates(subset=["order_id"])

    logging.info(f"Transformation completed: {len(df)} final rows")
    return df