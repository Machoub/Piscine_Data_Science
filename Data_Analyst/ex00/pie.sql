SELECT event_type, COUNT(*) AS pie_chart 
FROM customers 
GROUP BY event_type 
ORDER BY pie_chart DESC;