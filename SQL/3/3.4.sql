select max(NumberOfF)
from (select Subject, Num, count(StuID) as NumberOfF
from Enroll 
group by Subject, Num) t1;