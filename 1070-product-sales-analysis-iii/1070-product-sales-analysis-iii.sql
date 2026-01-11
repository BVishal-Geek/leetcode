With fyear as (
    Select product_id, min(year) as first_year
    from Sales 
    group by product_id
)

select S.product_id, f.first_year, S.quantity, S.price
from Sales S
Join fyear f
On S.product_id = f.product_id AND S.year = f.first_year;