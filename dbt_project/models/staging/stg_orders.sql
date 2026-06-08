SELECT order_id, customer_id, product_id, order_date::date AS order_date, quantity::int AS quantity FROM raw_orders
