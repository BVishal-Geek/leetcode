select p.unique_id, pl.name 
from Employees pl
left join EmployeeUNI p on pl.id = p.id; 