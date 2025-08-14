ALTER TABLE customers
ADD category_id bigint,
ADD category_code VARCHAR(255),
ADD brand VARCHAR(255);

UPDATE customers c
SET 
    category_id = i.category_id,
    category_code = i.category_code,
    brand = i.brand
FROM item i
WHERE c.product_id = i.product_id;


