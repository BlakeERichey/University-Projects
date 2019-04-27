SELECT 
  Person.First_Name  AS "ClientFirstName",
  Person.Middle_Name AS "ClientMiddleName",
  Person.Last_Name   AS "ClientLastName",
  VolunteerPerson.First_Name  AS "VolunteerFirstName",
  VolunteerPerson.Middle_Name AS "VolunteerMiddleName",
  VolunteerPerson.Last_Name   AS "VolunteerLastName",
  Volunteer.Date_Joined,
  Team.Name                   AS "Team Name"    
FROM Client
INNER JOIN Cares ON Client.id=Cares.Client_Id
INNER JOIN Team  ON Team.Name = Cares.Team_Name
INNER JOIN Works ON Works.Team_Name = Team.Name
INNER JOIN Volunteer ON Volunteer.id = Works.Volunteer_Id
INNER JOIN (
  SELECT * FROM Person
) VolunteerPerson ON (VolunteerPerson.id=Volunteer.Person_Id)
INNER JOIN Person ON Person.id = Client.Person_Id
WHERE Person.Gender != VolunteerPerson.Gender
ORDER BY "ClientLastName", "ClientFirstName", "Team Name", "VolunteerLastName",
  "VolunteerFirstName";