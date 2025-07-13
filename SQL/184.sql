# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
JOIN (
    SELECT departmentId, MAX(salary) AS maxSalary
    FROM Employee
    GROUP BY departmentId
) AS max_salaries
ON e.departmentId = max_salaries.departmentId AND e.salary = max_salaries.maxSalary;
