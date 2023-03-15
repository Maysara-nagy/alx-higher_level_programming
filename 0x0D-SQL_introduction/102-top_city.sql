-- 102-top_city.sql
SELECT city, MAX(value) AS avg_temp FROM temperatures ORDER BY avg_temp DESC LIMIT 3 WHERE month = 7 OR month = 8 GROUP BY city;