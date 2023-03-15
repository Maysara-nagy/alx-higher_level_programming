-- 102-top_city.sql
SELECT city, MAX(value) AS avg_temp FROM temperature ORDER BY avg_temp DESC LIMIT 3 WHERE month = 7 or month = 8 GROUP BY city;