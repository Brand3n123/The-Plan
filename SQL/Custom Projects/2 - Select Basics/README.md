# Baseline Log Integrity Checks (`01_select_basics.sql`)

## Overview
This script runs a few quick checks against the `events` table in hypothetical `sql_log_analyzer.db`.  
Reviews make sure log data looks normal — that new events are coming in, timestamps make sense, and nothing obvious is missing or broken.

---

## What It Does

| # | Purpose | SQL Feature | Why It’s Useful |
|---|----------|--------------|----------------|
| 1 | Look at the latest log entries | `ORDER BY ts DESC LIMIT` | Confirms logs are still updating. |
| 2 | Find failed provisioning events from the last 24h | `WHERE` + time filter | Verifies provisioning failures are being recorded. |
| 3 | List all event types in the table | `DISTINCT` | Quick check that expected categories exist. |
| 4 | Search for timeout errors | `LIKE 'E_T%'` | Helps spot recurring timeout issues. |
| 5 | See which users generate the most logs | `GROUP BY`, `COUNT`, `ORDER BY` | Flags noisy users or retry loops. |

---

## How to Run
```bash
sqlite3 sql_log_analyzer.db < sql/01_select_basics.sql