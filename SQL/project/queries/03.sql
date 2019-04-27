select person.first_name,volunteer.date_joined
from works,volunteer,team,cares,person
where cares.Client_Id = &clientId and volunteer.Person_id = person.id
 And
 works.volunteer_id=volunteer.id and works.team_name=team.name
 and 
 team.name=cares.team_name
 order by volunteer.date_joined;
