With first_login_date as (
    select player_id, min(event_date) as first_login
    from Activity 
    Group by player_id
)

Select Cast(Count(Distinct A.player_id)/(
    select count(distinct player_id) from Activity) AS Decimal(10,2)) As fraction
    From Activity A
    Join first_login_date F
    On F.player_id = A.player_id
    Where Datediff(A.event_date, F.first_login) = 1;