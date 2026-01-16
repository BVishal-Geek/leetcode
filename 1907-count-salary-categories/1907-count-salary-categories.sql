with static_table as (
SELECT 'Low Salary' AS category
UNION ALL
SELECT 'Average Salary'
UNION ALL
SELECT 'High Salary'
),
categories as (
select category, Count(*) as accounts_count from 
(
    select account_id, 
    CASE 
           WHEN income < 20000 THEN 'Low Salary'
           WHEN income <= 50000 THEN 'Average Salary'
           ELSE 'High Salary'
         END AS category
  FROM Accounts
) AS salary_categories
GROUP BY category
)

select st.category, Coalesce(c.accounts_count,0) as accounts_count
from static_table st 
left join categories c
on st.category = c.category
