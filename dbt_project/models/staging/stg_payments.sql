SELECT payment_id, order_id, payment_date::date AS payment_date, payment_amount::numeric AS payment_amount, payment_status FROM raw_payments
