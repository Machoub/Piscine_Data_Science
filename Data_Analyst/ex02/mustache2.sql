SELECT 
    user_id, 
    AVG(CAST(price AS float)) AS avg_price
FROM customers
WHERE event_type = 'cart'
GROUP BY user_id
HAVING AVG(CAST(price AS float)) BETWEEN 26 AND 43
LIMIT 100;