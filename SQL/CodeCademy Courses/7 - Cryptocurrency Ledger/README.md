Cryptocurrency Exchange — January Ledger (crypto_ledger_codecademy_project.sql)

Overview
Use aggregates to analyze a January transactions table for Fiddy Cent (Neo Tokyo). Focus: totals, largest tx, per-day averages, and “does BIT dominate?” checks.

Instructions (from Codecademy)

Explore the table and list column names.

Total money_in.

Total money_out.

Count money-in transactions overall and count where currency = 'BIT'.

Find the largest single transaction in the table and say if it was money_in or money_out.

Average money_in for 'ETH'.

Build a per-date ledger: date, avg money_in, avg money_out grouped by date.

Round those averages to 2 decimals and add readable aliases.

Code:

-- totals
SELECT SUM(money_in) FROM transactions;
SELECT SUM(money_out) FROM transactions;

-- money_in count for BIT
SELECT COUNT(money_in) FROM transactions 
WHERE currency = 'BIT';

-- largest transactions (compare)
SELECT MAX(money_in) FROM transactions;   -- 6000
SELECT MAX(money_out) FROM transactions;  -- 15047

-- avg money_in for ETH
SELECT AVG(money_in) FROM transactions 
WHERE currency = 'ETH';

-- daily averages
SELECT date, AVG(money_in), AVG(money_out) 
FROM transactions 
GROUP BY date;

-- rounded + aliases
SELECT date, 
  ROUND(AVG(money_in), 2) AS Deposits, 
  ROUND(AVG(money_out), 2) AS Withdrawals
FROM transactions 
GROUP BY date;



Concepts Used
SUM, COUNT, MAX, AVG, ROUND, GROUP BY, ORDER BY, basic filtering with WHERE