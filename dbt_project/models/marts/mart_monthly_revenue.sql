SELECT DATE_TRUNC('month', o.order_date)::date AS revenue_month, COUNT(DISTINCT o.order_id) AS total_orders, COUNT(DISTINCT o.customer_id) AS unique_customers, SUM(pay.payment_amount) AS total_paid_revenue
FROM {{ ref('fact_orders') }} o
LEFT JOIN {{ ref('stg_payments') }} pay ON o.order_id = pay.order_id
WHERE pay.payment_status = 'Success'
GROUP BY 1
ORDER BY 1
