-- 101-avg_temperatures.sql
SELECT city, AVG(value) AS avg_temp FROM temperatures ORDER BY temperature DESC GROUP BY city;