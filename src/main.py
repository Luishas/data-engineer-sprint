import logging
from  extract import extract_csv
from  transform import transform_generic
from  load import load_to_postgres

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

TABLES = [
    {"file": "olist_orders_dataset.csv", "table": "raw_orders", "key": "order_id"},
    {"file": "olist_order_items_dataset.csv", "table": "raw_order_items", "key": "order_id"},
    {"file": "olist_order_payments_dataset.csv", "table": "raw_order_payments", "key": "order_id"},
    {"file": "olist_order_reviews_dataset.csv", "table": "raw_order_reviews", "key": "review_id"},
    {"file": "olist_customers_dataset.csv", "table": "raw_customers", "key": "customer_id"},
    {"file": "olist_products_dataset.csv", "table": "raw_products", "key": "product_id"},
    {"file": "olist_sellers_dataset.csv", "table": "raw_sellers", "key": "seller_id"},
    {"file": "olist_geolocation_dataset.csv", "table": "raw_geolocation", "key": None},
    {"file": "product_category_name_translation.csv", "table": "raw_category_translation", "key": None},
]

def run_pipeline():
    logging.info("Starting ETL pipeline - orders")
    for t in TABLES:
        logging.info(f"--- Processing {t['table']} ---")
        df_raw = extract_csv(t["file"])
        df_clean = transform_generic(df_raw, t["key"]) if t["key"] else df_raw
        load_to_postgres(df_clean, table_name=t["table"])
    logging.info("ETL pipeline completed successfully: 9 uploaded tables")

if __name__ == "__main__":
    run_pipeline()