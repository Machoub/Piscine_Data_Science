SELECT user_id, event_time, event_type, CAST(price AS float)
FROM customers
WHERE event_type = 'purchase';