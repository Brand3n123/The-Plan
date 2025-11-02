-- Q2
-- SELECT * FROM places WHERE price_point <= '$$';

-- Q3 (join keys)
-- places.id & reviews.place_id

-- Q4: INNER JOIN (with extra filter)
SELECT * 
FROM places
JOIN reviews ON places.id = reviews.place_id
WHERE total_reviews > 0;

-- Q5: INNER JOIN with selected columns
SELECT places.name, places.average_rating, 
       reviews.username, reviews.rating, reviews.review_date, reviews.note
FROM places
JOIN reviews ON places.id = reviews.place_id
WHERE total_reviews > 0;

-- Q6: LEFT JOIN (but still filtered)
SELECT places.name, places.average_rating, 
       reviews.username, reviews.rating, reviews.review_date, reviews.note
FROM places
LEFT JOIN reviews ON places.id = reviews.place_id
WHERE total_reviews > 0;

-- Q7: places without reviews
SELECT places.id, places.name
FROM places
LEFT JOIN reviews ON places.id = reviews.place_id
WHERE reviews.place_id IS NULL;