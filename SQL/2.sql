insert into Course(Subject, Num, Title, Fee)
values('CS', 4385, 'Databases', 200);

insert into Course(Subject, Num, Title, Fee)
values('CS', 2336, 'Data Structures', 250);

insert into Course(Subject, Num, Title, Fee)
values('CS', 1336, 'OOP', 100);

insert into Course(Subject, Num, Title, Fee)
values('CS', 4315, 'Knowledge Management', 200);

insert into Course(Subject, Num, Title, Fee)
values('CS', 4352, 'Data Mining', 300);

insert into Course(Subject, Num, Title, Fee)
values('CORE', 5000, 'Capstone', 5000);

insert into Course(Subject, Num, Title, Fee)
values('MATH', 3351, 'Probability', 60);

insert into Course(Subject, Num, Title, Fee)
values('MATH', 2330, 'Calculus', 20);

insert into Course(Subject, Num, Title, Fee)
values('MATH', 1101, 'Algebra', 10);

insert into Course(Subject, Num, Title, Fee)
values('CORE', 1111, 'General Chemistry', 250);

INSERT ALL
into Student(StuID, StuName, Year, GPA) values (111, 'Mikayla',       'FR', 2.7)
into Student(StuID, StuName, Year, GPA) values (222, 'Lambda',        'SR', 3.7)
into Student(StuID, StuName, Year, GPA) values (333, 'Fireboy',       'SO', 3.5)
into Student(StuID, StuName, Year, GPA) values (444, 'Lame Guy',      'FR', 1.0)
into Student(StuID, StuName, Year, GPA) values (555, 'Blake Richey',  'SR', 3.8)
into Student(StuID, StuName, Year, GPA) values (666, 'James Kwon',    'JR', 3.6)
into Student(StuID, StuName, Year, GPA) values (777, 'Emily',         'SR', 3.6)
into Student(StuID, StuName, Year, GPA) values (888, 'Kaya Click',    'SO', 2.0)
into Student(StuID, StuName, Year, GPA) values (999, 'Tyler Andrews', 'JR', 2.9)
into Student(StuID, StuName, Year, GPA) values (987, 'Misc Guy',      'FR', 4.0)
SELECT * FROM dual;

INSERT ALL
into Enroll(StuID, Subject, Num, Grade) values(111, 'CS',   1336, 'B')
into Enroll(StuID, Subject, Num, Grade) values(222, 'MATH', 2345, 'A')
into Enroll(StuID, Subject, Num, Grade) values(333, 'CORE', 1111, 'A')
into Enroll(StuID, Subject, Num, Grade) values(444, 'CORE', 1111, 'F')
into Enroll(StuID, Subject, Num, Grade) values(555, 'CS',   4385, 'A')
into Enroll(StuID, Subject, Num, Grade) values(666, 'MATH', 2330, 'A')
into Enroll(StuID, Subject, Num, Grade) values(777, 'CORE', 5000, 'A')
into Enroll(StuID, Subject, Num, Grade) values(888, 'CS',   4315, 'B')
into Enroll(StuID, Subject, Num, Grade) values(999, 'MATH', 1101, 'A')
into Enroll(StuID, Subject, Num, Grade) values(987, 'MATH', 3351, 'C')
into Enroll(StuID, Subject, Num, Grade) values(555, 'CS',   4315, 'A')
into Enroll(StuID, Subject, Num, Grade) values(555, 'CS',   4352, 'A')
into Enroll(StuID, Subject, Num, Grade) values(555, 'CORE', 5000, 'B')
into Enroll(StuID, Subject, Num, Grade) values(555, 'MATH', 3351, 'B')
into Enroll(StuID, Subject, Num, Grade) values(555, 'CS',   2336, 'A')
into Enroll(StuID, Subject, Num, Grade) values(123, 'CS',   4385, 'C')
into Enroll(StuID, Subject, Num, Grade) values(234, 'CS',   1336, 'B')
into Enroll(StuID, Subject, Num, Grade) values(987, 'CORE', 1111, 'A')
into Enroll(StuID, Subject, Num, Grade) values(987, 'CS', 4352, 'B')
into Enroll(StuID, Subject, Num, Grade) values(987, 'CORE', 5000, 'A')
SELECT * FROM dual;