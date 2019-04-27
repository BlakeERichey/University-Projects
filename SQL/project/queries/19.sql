Select
          person.first_name,person.last_name,count(works.team_name),sum(works.hours)
          from volunteer,person,works WHERE volunteer.id = works.volunteer_id
          and person.id=volunteer.person_id and date_joined between
          TO_DATE (add_months(sysdate,-3), 'DD/MM/YY')
          AND
          TO_DATE (sysdate, 'DD/MM/YY')
          group by person.first_name,person.last_name
          order by person.last_name,person.first_name;
