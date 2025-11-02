--
SELECT COUNT(*) FROM events 
WHERE ts 
    BETWEEN 2025-10-22T13:15:00Z 
    AND 2025-10-22T13:30:00Z;

--

SELECT COUNT(*) AS fail_count,
    CASE 
        WHEN ts LIKE '2025-10-22T13:15%' THEN '13:15'
        WHEN ts LIKE '2025-10-22T13:16%' THEN '13:16'
        WHEN ts LIKE '2025-10-22T13:17%' THEN '13:17'
        WHEN ts LIKE '2025-10-22T13:18%' THEN '13:18'
        WHEN ts LIKE '2025-10-22T13:19%' THEN '13:19'
        WHEN ts LIKE '2025-10-22T13:20%' THEN '13:20'
        WHEN ts LIKE '2025-10-22T13:21%' THEN '13:21'
        WHEN ts LIKE '2025-10-22T13:22%' THEN '13:22'
        WHEN ts LIKE '2025-10-22T13:23%' THEN '13:23'
        WHEN ts LIKE '2025-10-22T13:24%' THEN '13:24'
        WHEN ts LIKE '2025-10-22T13:25%' THEN '13:25'
        WHEN ts LIKE '2025-10-22T13:26%' THEN '13:26'
        WHEN ts LIKE '2025-10-22T13:27%' THEN '13:27'
        WHEN ts LIKE '2025-10-22T13:28%' THEN '13:28'
        WHEN ts LIKE '2025-10-22T13:29%' THEN '13:29'
        WHEN ts LIKE '2025-10-22T13:30%' THEN '13:30'
        ELSE 'Other'
    END AS 'minute_label'
FROM events
WHERE result='fail'
GROUP BY minute_label
ORDER BY fail_count DESC LIMIT 1;
    
--    
SELECT device_id,
COUNT(*) as fail_count
FROM events
WHERE result='fail'
    AND ts 
    BETWEEN '2025-10-22T13:15:00Z' AND '2025-10-22T13:30:00Z'
GROUP BY device_id
ORDER BY fail_count DESC;

--
SELECT event_id,
error_code,
    CASE
        WHEN error_code = 'E_AUTH' THEN 'Provisioning Failure'
        WHEN error_code = 'E_TIMEOUT' THEN 'Network Failure'
        WHEN error_code IS NULL THEN 'Healthy'
        ELSE 'Other'
    END AS error_type
FROM events
WHERE result='fail'
    AND ts
    BETWEEN '2025-10-22T13:15:00Z' AND '2025-10-22T13:30:00Z';

--
SELECT error_code,
    CASE
        WHEN error_code = 'E_AUTH' THEN 'Provisioning Failure'
        WHEN error_code = 'E_TIMEOUT' THEN 'Network Failure'
        WHEN error_code IS NULL THEN 'Healthy'
        ELSE 'Other'
    END AS error_type
FROM events
WHERE result='fail'
    AND ts
    BETWEEN '2025-10-22T13:15:00Z' AND '2025-10-22T13:30:00Z'
GROUP BY error_type
ORDER BY COUNT(*) DESC;
