Select
person.first_name,person.last_name,person.street_address,person.city,
person.state,person.zipcode,person.profession,sum(donor_donations.amount)       as sum,donor_donations.anonymous
From
Client,person,donor,donor_donations
Where
client.person_id = person.id
And
donor.person_id=person.id
And
donor_donations.donor_id = donor.id
group by person.first_name,person.last_name,person.street_address,person.city,person.state,person.zipcode,person.profession,donor_donations.anonymous
 order by sum desc;
