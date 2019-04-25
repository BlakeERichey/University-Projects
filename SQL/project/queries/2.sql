SELECT 
    Person.Title         as Title, 
    Person.First_Name    as First, 
    Person.Middle_Name   as Middle, 
    Person.Last_Name     as Last, 
    Doctor.First_Name    as DoctorFirstName, 
    Doctor.Last_Name     as DoctorLastName, 
    Doctor.Doctor_Number as DoctorNumber
FROM CLIENT
INNER JOIN Doctor ON Doctor.Client_Id=Client.id
INNER JOIN Person ON Person.id=Client.Person_Id
ORDER BY Last ASC, First ASC;