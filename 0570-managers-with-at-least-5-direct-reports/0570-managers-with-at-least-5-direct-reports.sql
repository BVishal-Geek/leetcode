# Write your MySQL query statement below
with manager as 
(
    Select E1.id as id, E1.name as name, count(*) as employeeCount
    From Employee E1
    Join Employee E2
    On E1.id = E2.managerId
    Group by E1.id, E1.name
)

Select name from manager
Where employeeCount >=5;