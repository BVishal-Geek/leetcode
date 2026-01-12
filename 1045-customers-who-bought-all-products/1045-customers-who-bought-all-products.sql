WITH product_count AS (
  SELECT COUNT(DISTINCT product_key) AS productUniqueCount
  FROM Product
),
customer_product_count AS (
  SELECT customer_id, COUNT(DISTINCT product_key) AS customerProductCount
  FROM Customer
  GROUP BY customer_id
)
SELECT cpc.customer_id
FROM customer_product_count cpc
JOIN product_count pc
  ON cpc.customerProductCount = pc.productUniqueCount;