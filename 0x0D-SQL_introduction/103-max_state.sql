-- 103-max_state.sql
SELECT state, MAX(value) AS max_temp FROM temperatures ORDER BY state GROUP BY state;