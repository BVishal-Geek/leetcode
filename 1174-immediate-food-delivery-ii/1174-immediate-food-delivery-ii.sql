With delivery_status as (
    select customer_id, order_date, customer_pref_delivery_date, row_number() Over(partition by customer_id order by order_date asc) as rnk, CASE When DATEDIFF(order_date, customer_pref_delivery_date)=0 Then 1 ELSE 0 END AS status_count
    from Delivery
)

Select CAST(AVG(status_count) * 100 AS DECIMAL(10,2)) as immediate_percentage
from delivery_status 
where rnk=1;