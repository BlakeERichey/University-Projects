select  organization.type,sum(amount),count(Org_donations.id) from
            organization,Org_Donations 
where organization.name = Org_donations.Org_Name
 group by organization.type;
