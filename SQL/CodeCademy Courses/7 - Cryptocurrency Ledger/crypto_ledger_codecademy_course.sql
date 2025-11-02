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