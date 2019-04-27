--Clients that are supported by team that reports to highest paid employee
SELECT 
    Person.Title          as Title, 
    Person.First_Name     as First, 
    Person.Middle_Name    as Middle, 
    Person.Last_Name      as Last,
    Person.Street_Address as StreetAddress,
    Person.City,
    Person.State,
    Person.Zipcode 
FROM Employee 
INNER JOIN Team   ON Team.Reports_To=Employee.id
INNER JOIN Cares  ON Cares.Team_Name=Team.Name
INNER JOIN Client ON Client.id=Cares.Client_Id
INNER JOIN Person ON Person.id=Client.Person_Id
WHERE (Monthly_Salary) IN 
( SELECT MAX(Monthly_Salary)
  FROM Employee
)
ORDER BY Last ASC;