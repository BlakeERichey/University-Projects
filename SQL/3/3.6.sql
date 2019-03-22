create view ClassSize as
select Subject, Num, count(StuID) as NumStudents
from Enroll 
group by Subject, Num;

select Subject, Num
from ClassSize
where NumStudents in select max(NumStudents) from ClassSize;