SELECT 
  Donation_Drive.Title,
  Donation_Drive.End_Date,
  Person.Last_Name,
  Employee.Job_Title
FROM Donation_Drive
LEFT OUTER JOIN Employee ON Employee.id = Donation_Drive.Employee_Id
LEFT OUTER JOIN Person ON Person.id = Employee.Person_Id
WHERE Donation_Drive.Title IN(
  SELECT 
    Donation_Drive.Title
  FROM Donation_Drive
  LEFT OUTER JOIN Donor_Donations ON Donor_Donations.Donation_Drive_Title=Donation_Drive.Title
  GROUP BY Donation_Drive.Title, Donation_Drive.Goal
  HAVING SUM(NVL(Donor_Donations.Amount, 0)) <= Donation_Drive.Goal
)
ORDER BY Donation_Drive.Goal DESC;