---None in database that match this query
SELECT 
    Need
FROM Client
INNER JOIN Needs ON Needs.Client_Id=Client.id
WHERE Needs.Importance >= 7
GROUP BY Needs.Need
HAVING Count(Need) >= 2;