-- select person_name from (
--     select person_name, Sum(weight) Over(Order by turn asc) as total_weight
--     from Queue
--     ) as E
--     where total_weight <= 1000
--     order by total_weight desc
--     limit 1;


select person_name from
(
    select person_name, turn, (select sum(weight) from Queue q2 where q2.turn <= q1.turn ) as total_weight
    from Queue q1
) as E
where total_weight<=1000
order by total_weight desc 
limit 1;