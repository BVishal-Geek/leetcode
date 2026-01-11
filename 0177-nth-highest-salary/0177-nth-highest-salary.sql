CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select distinct E1.salary as getNthHighestSalary
      From Employee E1
      Where N = (Select Count(Distinct E2.salary)
                from Employee E2
                Where E2.salary >= E1.salary)
  );
END