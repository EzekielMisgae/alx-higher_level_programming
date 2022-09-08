-- top 3 cities avg in August and July
SELECT `city`, AVG(`value`) 'avg_temp' FROM temperatures WHERE month = 8 OR month = 7 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3 ;