update needs set importance=(importance+1)
                      where needs.client_id in
                      (SELECT EMPLOYEE.ID FROM EMPLOYEE,MEETINGS
                      WHERE EMPLOYEE.ID=MEETINGS.EMPLOYEE_ID
                      having count(meetings.employee_id) <>
                      (select min(employee.id) from employee,meetings
                      where employee.id = meetings.employee_id fetch next 1 rows only)
                      GROUP BY EMPLOYEE.ID);
