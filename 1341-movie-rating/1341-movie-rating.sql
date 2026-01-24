WITH cte1 AS (
    SELECT user_id, COUNT(movie_id) AS movieCounts
    FROM MovieRating
    GROUP BY user_id
),
cte2 AS (
    SELECT movie_id, AVG(rating) AS avgRating
    FROM MovieRating
    WHERE EXTRACT(YEAR FROM created_at) = 2020
      AND EXTRACT(MONTH FROM created_at) = 2
    GROUP BY movie_id
)

(SELECT U.name AS results
FROM cte1 c1
LEFT JOIN Users U ON U.user_id = c1.user_id
WHERE c1.movieCounts = (SELECT MAX(movieCounts) FROM cte1)
ORDER BY U.name asc
LIMIT 1)

UNION ALL

(SELECT M.title AS results
FROM cte2 c2
LEFT JOIN Movies M ON M.movie_id = c2.movie_id
WHERE c2.avgRating = (SELECT MAX(avgRating) FROM cte2)
ORDER BY M.title asc
LIMIT 1);