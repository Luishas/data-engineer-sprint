CREATE OR REPLACE VIEW clean_sales AS
SELECT
    o.order_id,
    o.customer_id,
    o.purchase_date,
    oi.product_id,
    oi.price
FROM staging_orders o
JOIN raw_order_items oi ON o.order_id = oi.order_id
WHERE oi.price > 0;