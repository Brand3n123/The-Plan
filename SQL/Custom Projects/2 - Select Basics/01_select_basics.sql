--Challenge 1
SELECT ts 
FROM events 
ORDER BY ts 
DESC LIMIT 10;

--Challenge 2
SELECT event_id, event_type, ts, error_code 
FROM events 
WHERE event_type='provision'
    AND result='fail' 
    AND ts >= datetime('now', '-1 day') 
ORDER BY ts DESC;

--Challenge 3
SELECT DISTINCT event_type 
FROM events
ORDER BY event_type;

--Challenge 4
SELECT event_id, error_code 
FROM events 
WHERE error_code 
    LIKE 'E_T%';

--Challenge 5
SELECT user_id, COUNT(user_id) 
FROM events
GROUP BY user_id 
ORDER BY total_events DESC;