# API Latency and Call Classification (CASE Challenge)

## 🧭 Overview
This SQL script (`02_case_api_logs.sql`) demonstrates how conditional logic (`CASE` statements) can be used to classify raw API log data into meaningful diagnostic categories.  
In a real-time support or network operations context (e.g., EchoStar / Boost Mobile backend), this approach helps engineers quickly identify **slow responses** and **failed API calls** without requiring post-processing in another tool.

---

## ⚙️ What the Script Does
The query reads from an `api_logs` table that tracks device-level API requests:

| Column | Description |
|---------|--------------|
| `device_id` | Unique device identifier |
| `latency_ms` | API response latency in milliseconds |
| `http_status` | HTTP status code returned by the request |

It then applies two `CASE` expressions to translate these raw values into human-readable labels:

1. **`latency_grade`** — classifies performance based on response time  
≤300 ms → Excellent
≤800 ms → Good
≤1500 ms → Fair

1500 ms → Poor

csharp
Copy code

2. **`call_status`** — categorizes result based on HTTP status  
200–299 → Success
400–499 → Client Error
≥500 → Server Error

yaml
Copy code

Finally, results are ordered from slowest to fastest (`ORDER BY latency_ms DESC`), making it easy to spot high-latency or failed calls at the top of the list.

---

## 🧩 Example Output

| device_id | latency_ms | http_status | latency_grade | call_status |
|------------|-------------|--------------|----------------|--------------|
| 103 | 2400 | 503 | Poor | Server Error |
| 101 | 1275 | 200 | Fair | Success |
| 102 | 420  | 404 | Good | Client Error |
| 104 | 150  | 200 | Excellent | Success |

---

## 💡 Practical Usage
Support engineers can use this query to:
- Monitor **API performance health** directly in SQL.
- Identify **outlier latency spikes** by device or endpoint.
- Correlate **HTTP 5xx errors** with high latency patterns.
- Generate quick operational reports for a given timeframe:
```sql
SELECT * FROM api_logs
WHERE http_status >= 500
ORDER BY latency_ms DESC;
🧰 How to Run
If using SQLite locally:

bash
Copy code
sqlite3 sql_log_analyzer.db < 02_case_api_logs.sql
If using another RDBMS, adjust syntax for your dialect (ANSI-SQL compliant).