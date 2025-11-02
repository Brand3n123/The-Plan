-- 1–2
SELECT * FROM employees LIMIT 1;
SELECT * FROM projects LIMIT 1;
-- join key: employees.current_project = projects.project_id

-- 3
SELECT first_name, last_name
FROM employees
WHERE current_project IS NULL;

-- 4
SELECT project_name
FROM projects
LEFT JOIN employees
  ON employees.current_project = projects.project_id
WHERE employee_id IS NULL;

-- 5 (CTE attempt)
WITH 'combined_table' AS (
  SELECT *
  FROM employees
  JOIN projects
    ON employees.current_project = projects.project_id
)
SELECT project_name, COUNT(project_name)
FROM combined_table
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- 6 (CTE attempt with CROSS JOIN)
WITH 'combined_table' AS (
  SELECT *
  FROM employees
  CROSS JOIN projects
    ON employees.current_project = projects.project_id
)
SELECT project_name, COUNT(project_id) AS 'qty'
FROM combined_table
GROUP BY project_name
HAVING qty > 1;