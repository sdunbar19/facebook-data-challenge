SELECT country, COUNT(show_id) as counts
FROM netflix
GROUP BY country
ORDER BY counts DESC
LIMIT 15;

SELECT YEAR(date_added), COUNT(show_id) AS counts
FROM netflix
GROUP BY year(date_added)
ORDER BY year(date_added) DESC;