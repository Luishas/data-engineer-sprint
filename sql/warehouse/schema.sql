CREATE TABLE dim_customers (
    customer_sk SERIAL PRIMARY KEY,
    customer_id VARCHAR UNIQUE,
    customer_city VARCHAR,
    customer_state VARCHAR
);

CREATE TABLE dim_products (
    product_sk SERIAL PRIMARY KEY,
    product_id VARCHAR UNIQUE,
    product_category_name VARCHAR
);

CREATE TABLE dim_sellers(
    seller_sk SERIAL PRIMARY KEY,
    seller_id VARCHAR UNIQUE,
    seller_ciry VARCHAR,
    seller_state VARCHAR
);

CREATE TABLE dim_date (
    date_sk SERIAL PRIMARY KEY,
    full_date DATE UNIQUE,
    year INT,
    month INT,
    day INT,
    weekday VARCHAR
);

CREATE TABLE fact_sales(
    fact_sk SERIAL PRIMARY KEY,
    order_id VARCHAR,
    customer_sk INT REFERENCES dim_customers(customer_sk),
    product_sk INT REFERENCES dim_products(product_sk),
    seller_sk INT REFERENCES dim_sellers(seller_sk),
    date_sk INT REFERENCES dim_date(date_sk),
    price NUMERIC,
    freight_value NUMERIC
);