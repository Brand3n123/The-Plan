SELECT device_id, latency_ms, http_status,
    CASE
        WHEN latency_ms <= 300 THEN 'Excellent'
        WHEN latency_ms <= 800 THEN 'Good'
        WHEN latency_ms <= 1500 THEN 'Fair'
        WHEN latency_ms > 1500 THEN 'Poor'
    END AS latency_grade,

    CASE
        WHEN http_status BETWEEN 200 AND 299 THEN "Success"
        WHEN http_status BETWEEN 400 AND 499 THEN "Client Error"
        WHEN http_status >= 500 THEN "Server Error"
    END AS call_status

FROM api_logs    
ORDER BY latency_ms DESC;