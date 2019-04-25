--INCOMPLETE

DROP VIEW "Person.Ethnicity";

---NUMBER OF ETHNICITIES REGARDLESS OF GENDER
CREATE VIEW "Person.Ethnicity" AS
SELECT 
    Ethnicity, 
    COUNT(Ethnicity) as "Num Ethnicity"
FROM Person
GROUP BY Ethnicity;

---NUM CLIENTS BY ETHNICITY AND GENDER
SELECT 
    Person.Ethnicity, 
    Person.Gender, 
    COUNT(Client.id) as "Num Clients"
FROM Person
INNER JOIN Client ON Client.Person_Id=Person.id
GROUP BY Person.Ethnicity, Person.Gender;

---NUMBER OF GENDER REGARDLESS OF ETHNICITY
SELECT 
    Gender,
    COUNT(Gender)
FROM Person
GROUP BY Gender;