Multiple Tables with Reddit (reddit_multi_tables.sql)

Overview
Practice joining users, posts, and subreddits to answer common analytics questions: counts, “top-k”, and per-entity summaries.

Instructions (from Codecademy)

Inspect each table; show first 10 rows and list column names.

Identify primary keys and foreign keys.

Count how many subreddits exist.

Find:

user with the highest user score

post with the highest post score

top 5 subreddits by subscriber_count

LEFT JOIN users → posts to get posts per user, ordered by count desc.

INNER JOIN to show existing posts by active users (posts as the left table).

Stack posts2 under posts (UNION).

WITH popular_posts (score ≥ 5000), join to subreddits; show subreddit name, post title, score; order by score desc.

Highest-scoring post for each subreddit.

Average post score per subreddit (JOIN + AVG + GROUP BY).

Code (your version)

-- 1
SELECT * FROM users LIMIT 1;
SELECT * FROM posts LIMIT 1;
SELECT * FROM subreddits LIMIT 1;

-- (noted)
-- users:    id, username, email, join_date, score
-- posts:    id, title, user_id, subreddit_id, score, created_date
-- subreddits: id, name, created_date, subscriber_count

-- 2 (noted)
-- PK: users.id, posts.id, subreddits.id
-- FK: posts.user_id, posts.subreddit_id

-- 3
SELECT COUNT(*) FROM subreddits;

-- 4
SELECT users.username, MAX(posts.score)
FROM posts
JOIN users ON users.id = posts.user_id;

SELECT title, MAX(score) FROM posts;

SELECT name, subscriber_count
FROM subreddits
ORDER BY subscriber_count DESC
LIMIT 5;

-- 5
SELECT users.username, COUNT(posts.id)
FROM users
LEFT JOIN posts ON users.id = posts.user_id
GROUP BY users.id
ORDER BY 2 DESC;

-- 6
SELECT *
FROM posts
JOIN users ON posts.user_id = users.id;

-- 7
SELECT * FROM posts
UNION
SELECT * FROM posts2;

-- 8
WITH popular_posts AS (
  SELECT * FROM posts WHERE score >= 5000
)
SELECT subreddits.name, popular_posts.title, popular_posts.score
FROM subreddits
JOIN popular_posts ON popular_posts.subreddit_id = subreddits.id
ORDER BY popular_posts.score DESC;

-- 9
SELECT posts.title, subreddits.name, MAX(posts.score)
FROM subreddits
JOIN posts ON posts.subreddit_id = subreddits.id
GROUP BY subreddits.id;

--10
SELECT subreddits.name, AVG(posts.score)
FROM subreddits
JOIN posts ON subreddits.id = posts.subreddit_id
GROUP BY subreddits.name;



Concepts Used
Inspection, keys, COUNT, MAX, AVG, ORDER BY, LIMIT, LEFT JOIN, INNER JOIN, anti-join reasoning, UNION, CTE (WITH), “top-1-per-group” via subquery.