CREATE TABLE IF NOT EXISTS raw_customers (customer_id TEXT, first_name TEXT, last_name TEXT, email TEXT, country TEXT, signup_date DATE);
CREATE TABLE IF NOT EXISTS raw_products (product_id TEXT, product_name TEXT, category TEXT, price NUMERIC);
CREATE TABLE IF NOT EXISTS raw_orders (order_id TEXT, customer_id TEXT, product_id TEXT, order_date DATE, quantity INTEGER);
CREATE TABLE IF NOT EXISTS raw_payments (payment_id TEXT, order_id TEXT, payment_date DATE, payment_amount NUMERIC, payment_status TEXT);
CREATE TABLE IF NOT EXISTS raw_refunds (refund_id TEXT, order_id TEXT, refund_date DATE, refund_amount NUMERIC, refund_reason TEXT);
