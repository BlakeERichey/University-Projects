select SUM(Fee)
from (Enroll NATURAL JOIN Course)
where StuID in &StuID
group by StuID;