SELECT user_id, SUM(CAST(price AS FLOAT))
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id
HAVING SUM(CAST(price AS FLOAT)) < 225;