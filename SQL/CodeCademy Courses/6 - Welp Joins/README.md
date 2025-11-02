Overview
Practice joining places and reviews to explore review logs and uncover places without reviews.

Instructions (from Codecademy)

Inspect both tables:

SELECT * FROM places;  
SELECT * FROM reviews;


If each $ equals $10, find places that cost $20 or less.

Identify the columns you can use to JOIN the tables.

Do an INNER JOIN to show all reviews for places that have at least one review.

Modify the query to select only:

From places: name, average_rating

From reviews: username, rating, review_date, note

Do a LEFT JOIN selecting the same columns. How do results differ vs INNER JOIN? Which is better for a “review log”?

Find ids of places with no reviews.

Code (your version)

-- Q2 (commented in your file)
-- SELECT * FROM places WHERE price_point <= '$$';

-- Q3 (join keys, noted by you)
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


Concepts Used
INNER JOIN, LEFT JOIN, join keys, anti-join pattern (LEFT JOIN ... IS NULL), filtering, projection, ordering.