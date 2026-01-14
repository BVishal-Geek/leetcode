with filter_date as (
    select *
    from Products
    where change_date <= "2019-08-16"
), 
rank_prices as (
    SELECT *,
           RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rnk
    from filter_date
)

select uniq_ids.product_id, Coalesce(rp.new_price, 10) as price
from (select distinct product_id from Products) as uniq_ids
Left join rank_prices rp 
On uniq_ids.product_id = rp.product_id and rp.rnk=1;