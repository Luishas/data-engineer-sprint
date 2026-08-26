CREATE OR REPLACE VIEW staging_orders AS
SELECT 
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp::date AS purchase_date
FROM raw_orders,
WHERE order_id IS NOT NULL;