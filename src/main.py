import logging
from  extract import extract_csv
from  transform import transform_generic
from  load import load_to_postgres
from data_quality import check_nulls, check_duplicates, check_range, check_referential_integrity

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
    dataframes = {}

    for t in TABLES:
        logging.info(f"--- Processing {t['table']} ---")
        df_raw = extract_csv(t["file"])
        df_clean = transform_generic(df_raw, t["key"]) if t["key"] else df_raw
        load_to_postgres(df_clean, table_name=t["table"])

        dataframes[t["table"]] = df_clean

        if t["key"]:
            nulls = check_nulls(df_clean, t["key"])
            duplicates = check_duplicates(df_clean, t["key"])
            if nulls > 0 or duplicates > 0:
                logging.warning(f"{t['table']}: {nulls} nulls, {duplicates} duplicates detected after post-transformation checks")

    huerfan = check_referential_integrity(
        dataframes["raw_order_items"], dataframes["raw_orders"],
        "order_id", "order_id"
    )
    logging.info(f"order_items integrity check(no match in orders): {huerfan}")
    logging.info("ETL pipeline completed successfully: 9 uploaded tables")

if __name__ == "__main__":
    run_pipeline()