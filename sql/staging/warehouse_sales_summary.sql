CREATE OR REPLACE VIEW warehouse_sales_summary AS
SELECT
    customer_id,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(price) AS total_sales
FROM clean_sales
GROUP BY customer_id;