-- 1
-- What are the column names?
id, user_id, order_date, restaurant_id, item_name, special_instructions


-- 2 
-- How recent is this data?

SELECT DISTINCT order_date FROM orders
ORDER BY order_date 
DESC;

-- 3
-- Instead of selecting all the columns using *, 
-- write a query that selects only the special_instructions column.

-- Limit the result to 20 rows.

SELECT special_instructions 
FROM orders LIMIT 20;

-- 4 
-- Can you edit the query so that we are only 
-- returning the special instructions that are not empty?

SELECT special_instructions FROM orders 
WHERE special_instructions IS NOT NULL 
LIMIT 20;

-- 5
-- Let’s go even further and sort the instructions 
-- in alphabetical order (A-Z).
SELECT special_instructions FROM orders
WHERE special_instructions IS NOT NULL 
ORDER BY special_instructions 
LIMIT 20;

-- 6
-- Let’s search for special instructions that have the word ‘sauce’.

-- Are there any funny or interesting ones? 

SELECT special_instructions FROM orders 
WHERE special_instructions IS NOT NULL 
    AND special_instructions 
    LIKE '%sauce%' 
    ORDER BY special_instructions 
    LIMIT 20;

-- 7
-- Let’s search for special instructions that have the word ‘door’.
-- Any funny or interesting ones?

SELECT special_instructions FROM orders 
WHERE special_instructions IS NOT NULL 
    AND special_instructions LIKE '%door%' 
    ORDER BY special_instructions LIMIT 20;

-- 8
-- Let’s search for special instructions that have the word ‘box’.
-- Any funny or interesting ones?
SELECT special_instructions FROM orders 
WHERE special_instructions IS NOT NULL 
    AND special_instructions LIKE '%box%' 
    ORDER BY special_instructions LIMIT 20;

-- 9
-- Instead of just returning the special instructions, also return their order ids.
SELECT id, special_instructions FROM orders 
WHERE special_instructions IS NOT NULL 
ORDER BY special_instructions LIMIT 20;

-- For more readability:
-- Rename id as ‘#’
-- Rename special_instructions as ‘Notes’

SELECT id AS '#', 
special_instructions AS 'Notes'
FROM orders 
WHERE special_instructions IS NOT NULL 
ORDER BY special_instructions LIMIT 20;

"Cleanse yourself with the sage in the mailbox."
"Draw a dragon fighting flamingo on the pizza box."
"I live in the Tiny House in the backyard - behind the Oak."