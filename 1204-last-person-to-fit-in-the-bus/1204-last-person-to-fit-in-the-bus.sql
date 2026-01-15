select person_name from (
    select person_name, Sum(weight) Over(Order by turn asc) as total_weight
    from Queue
    ) as E
    where total_weight <= 1000
    order by total_weight desc
    limit 1;
