WITH cte AS (

SELECT  id,
        recordDate,
        temperature,
        DATEDIFF(recordDate, LAG(recordDate) OVER(ORDER BY recordDate)) AS DateDifference,
        temperature - LAG(temperature) OVER(ORDER BY recordDate) AS Diff
    FROM Weather
)

SELECT id FROM cte
WHERE diff > 0 AND DateDifference = 1;