UPDATE Org_Donations
SET Amount = Amount*2
WHERE Org_Donations."Date" IN(
  SELECT
    MAX(Org_Donations."Date")
  FROM Org_Donations
);