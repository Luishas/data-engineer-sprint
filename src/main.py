import logging
from  extract import extract_orders
from  transform import transform_orders
from  load import load_to_postgres

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_pipeline():
    logging.info("Starting ETL pipeline - orders")
    df_raw = extract_orders()
    df_clean = transform_orders(df_raw)
    load_to_postgres(df_clean)
    logging.info("ETL pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()