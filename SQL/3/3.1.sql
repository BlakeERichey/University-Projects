select StuName, Title, Grade
from (Student NATURAL JOIN Enroll) NATURAL JOIN Course
where Year = 'SR'
order by StuName;