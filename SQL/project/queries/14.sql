SELECT DISTINCT *
FROM (
  SELECT 
    Team.Name,
    Team.Type,
    LeaderPerson.First_Name         AS "LeaderFirstName",
    LeaderPerson.Last_Name          AS "LeaderLastName",
    Person.First_Name               AS "ReportToFirstName",
    Person.Last_Name                AS "ReportToLastName",
    CountVolunteers."NumVolunteers" AS "NumVolunteers",
    CountVolunteers."Hours"         AS "SumHours",
    MeetDates."Date"                AS "Date"
  FROM Team
  LEFT OUTER JOIN Works     ON Works.Team_Name=Team.Name
  LEFT OUTER JOIN Volunteer ON Volunteer.id=Works.Volunteer_Id
  LEFT OUTER JOIN (
  SELECT * FROM Person
  ) LeaderPerson ON (LeaderPerson.id=Team.Team_Leader)
  LEFT OUTER JOIN Person ON Person.id=Team.Reports_To
  LEFT OUTER JOIN( 
    SELECT 
      Team.Name             AS "Name",
      COUNT(Volunteer_Id)   AS "NumVolunteers",
      SUM(Works.Hours)      AS "Hours"
    FROM Team
    INNER JOIN Works ON Works.Team_Name=Team.Name
    GROUP BY Team.Name
  ) CountVolunteers ON CountVolunteers."Name"=Team.Name
  FULL OUTER JOIN(
    SELECT 
      Team_Name,
      MAX("Date") AS "Date"
    FROM Meetings
    GROUP BY Team_Name
  ) MeetDates ON MeetDates.Team_Name=Team.Name
)
ORDER BY Type ASC, Name ASC;