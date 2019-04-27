select organization.name, 
sum(donor_donations.amount)+sum(Org_donations.amount)
from person,organization,donor,donor_donations,Org_donations where
org_donations.org_name = organization.name and
organization.person_id = person.id and person.id=donor.person_id
and donor_donations.donor_id=donor.id group by organization.name
order by organization.name;
