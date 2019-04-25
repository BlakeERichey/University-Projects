SELECT 
    Person.Title              as Title, 
    Person.Last_Name          as Last,
    Phone_Number.Phone_Number as "Number",
    Donor_Donations."Date"    as "Date",
    Donor_Donations.Amount
FROM Donor
INNER JOIN Donor_Donations ON Donor_Donations.Donor_Id=Donor.id
INNER JOIN Person          ON Person.id=Donor.Person_Id
INNER JOIN Phone_Number    ON Phone_Number.Person_Id=Person.id
WHERE (Donor_Donations.Donor_Id, Donor_Donations."Date") IN (
    SELECT Donor_Id, MAX("Date") as "Date" 
    FROM Donor_Donations 
    GROUP BY Donor_Id
)
AND Donor_Donations.Anonymous = 'Y'
AND Phone_Number.Primary = 'Y'
AND Person.Mail_To = 'N'
ORDER BY Donor_Donations.Amount DESC;