-- select employee_id 
-- from (select a.employee_id, a.name, a.manager_id, a.salary 
--         from Employees a
--         join Employees b
--         where b.manager_id = a.employee_id
--         and a.salary <30000) as e


select employee_id 
from Employees
where manager_id Not in (select employee_id from Employees) and salary<30000
order by employee_id asc