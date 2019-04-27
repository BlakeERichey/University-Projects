select person.first_name fName,person.last_name lName,phone_number.phone_number Phone#, extract(year from donor_donations."Date")year
from
donor,donor_donations,person,phone_number
where
phone_number.person_id = person.id and phone_number.primary='Y' and person.id=donor.person_id and donor.id = donor_donations.donor_id
group by person.first_name,person.last_name,phone_number.phone_number,donor_donations."Date"
having (sum(donor_donations.amount)
in
	(select sum(donor_donations.amount)
	 from
	 donor,donor_donations 
	 where donor.id = donor_donations.donor_id
	 group by donor.id));