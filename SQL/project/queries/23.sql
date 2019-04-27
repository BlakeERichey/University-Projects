delete from employee where employee.id in (select id from (
select employee.id,count(meetings.employee_id) as count_meetings
from meetings right outer join employee on
employee.id = meetings.employee_id group by employee.id)x
having min(x.count_meetings) = 0 group by id);
