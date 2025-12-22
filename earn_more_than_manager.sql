# Write your MySQL query statement below
# WAY 1: Use subquery
-- SELECT name as Employee
-- FROM Employee e
-- WHERE salary > (SELECT salary
--     FROM Employee
--     WHERE id = e.managerId)

# WAY 2: Use inner join
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
    ON m.id = e.managerId
WHERE e.salary > m.salary

# WAY 3: Use EXISTS
-- SELECT e.name as Employee
-- FROM Employee e
-- WHERE EXISTS (
--     SELECT 1
--     FROM Employee m
--     WHERE m.id = e.managerId 
--         AND e.salary > m.salary
-- )

