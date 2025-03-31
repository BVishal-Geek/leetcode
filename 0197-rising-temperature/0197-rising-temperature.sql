-- WITH cte AS (

-- SELECT  id,
--         recordDate,
--         temperature,
--         DATEDIFF(recordDate, LAG(recordDate) OVER(ORDER BY recordDate)) AS DateDifference,
--         temperature - LAG(temperature) OVER(ORDER BY recordDate) AS Diff
--     FROM Weather
-- )

-- SELECT id FROM cte
-- WHERE diff > 0 AND DateDifference = 1;


-- SELF JOIN
SELECT W1.id
FROM Weather W1
JOIN Weather W2
ON DATEDIFF(W1.recordDate, W2.recordDate) = 1
WHERE w1.temperature > W2.temperature;