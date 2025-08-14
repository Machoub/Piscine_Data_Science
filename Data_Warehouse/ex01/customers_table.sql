CREATE TABLE IF NOT EXISTS customers AS (
    SELECT * FROM data_2022_dec
    UNION ALL
    SELECT * FROM data_2022_nov
    UNION ALL
    SELECT * FROM data_2022_oct
);