# Write your MySQL query statement below
SELECT e.name
FROM Employee e
INNER JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) AS sub ON e.id = sub.managerId;