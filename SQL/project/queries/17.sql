Select
Person.last_name,employee.monthly_salary,employee.marital_status,
count(team.reports_to),count(donation_drive.employee_id)
from person,employee,team,donation_drive
Where
donation_drive.employee_id = employee.id and person.id = employee.person_id
And
employee.type='PART-TIME' and team.reports_to = employee.id
group by person.last_name,employee.monthly_salary,employee.marital_status order by person.last_name;
