UPDATE Employee
SET Monthly_Salary = Monthly_Salary*1.1
WHERE Employee.id IN(
  SELECT 
    Employee.id
  FROM Team
  INNER JOIN Employee ON Employee.id=Team.Reports_To
  GROUP BY Employee.id
  HAVING COUNT(Team.Name) > 1
)
AND Type='PART-TIME';