/* SELECT
    CASE
        WHEN purchase_months = 4 THEN 'loyal platinum'
        WHEN purchase_months = 3 THEN 'loyal gold'
        WHEN purchase_months = 2 THEN 'loyal silver'
        WHEN purchase_months = 1 AND purchase_month = 1 THEN 'new customer'
        WHEN purchase_months = 1 AND purchase_month <> 1 THEN 'inactive'
    END AS purchase_months_category,
    COUNT(DISTINCT user_id) AS customer_count
FROM (
    SELECT 
        user_id,
        COUNT(DISTINCT EXTRACT(MONTH FROM event_time)) AS purchase_months,
        EXTRACT(MONTH FROM MIN(event_time)) AS purchase_month
    FROM customers
    WHERE event_type = 'purchase'
    GROUP BY user_id
) AS purchase_counts
GROUP BY purchase_months_category
ORDER BY customer_count; */

SELECT 
    user_id,
    COUNT(*) AS nbr_achats
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id
ORDER BY nbr_achats DESC;