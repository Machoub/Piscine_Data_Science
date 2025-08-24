SELECT user_id, COUNT(*) AS order_count, SUM(price) AS total_spent
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id
ORDER BY order_count DESC;