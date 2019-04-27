Select
person.first_name,person.last_name,sum(expenses.amount),
employee.monthly_salary
From
person,employee,expenses where employee.person_id = person.id
and expenses.employee_id=employee.id
group by person.first_name,person.last_name,employee.monthly_salary
having sum(expenses.amount) < employee.monthly_salary;
