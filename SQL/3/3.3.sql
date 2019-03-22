select Title
from Course
where Fee in (select max(Fee) from Course);