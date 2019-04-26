DELETE FROM Volunteer
WHERE Volunteer.id = (
  SELECT 
    Volunteer_Id 
  FROM Works
  WHERE Works.Hours IN(
    SELECT
      MIN(Hours)
    FROM Volunteer
    INNER JOIN Works ON Works.Volunteer_Id=Volunteer.id
  )
);