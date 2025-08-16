SELECT 
    TO_CHAR(event_time, 'Mon') AS month,
	ROUND(SUM(price) / 1000000, 1) AS total_price
FROM customers
WHERE event_type = 'purchase'
GROUP BY TO_CHAR(event_time, 'Mon')
ORDER BY MIN(event_time);