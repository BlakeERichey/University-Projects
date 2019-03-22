update Course
set Fee = Fee * 2
where upper(Title) like '%D%' OR upper(Title) like '%B%';