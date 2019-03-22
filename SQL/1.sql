drop table Enroll;
drop table Course;
drop table Student;

create table Student (
    StuID number,
    StuName varchar2(20),
    Year char(2),
    GPA number(2, 1),
    primary key(StuID),
    check(GPA between 0 and 4),
    check(Year IN('FR', 'SO', 'JR', 'SR'))
);

create table Course(
  Subject varchar2(4),
  Num number(4,0),
  Title varchar2(20),
  Fee number(6, 2),
  primary key(Subject, Num),
  check(Fee >= 0)
);

create table Enroll(
  StuID number,
  Subject varchar2(4),
  Num number(4,0),
  Grade char(1),
  primary key(StuID, Subject, Num),
  foreign key(StuID) references Student on delete cascade,
  foreign key(Subject, Num) references Course on delete cascade,
  check(Grade IN('A', 'B', 'C', 'D', 'F'))
);

insert into Student(StuID, StuName, Year, GPA)
values(123, 'Alpha', 'SR', 3.5);

insert into Student(StuID, StuName, Year, GPA)
values(234, 'Beta', 'SR', 2.8);

insert into Student(StuID, StuName, Year, GPA)
values(345, 'Gamma', 'JR', 3.3);

insert into Student(StuID, StuName, Year, GPA)
values(456, 'Delta', 'SO', 2.5);

insert into Student(StuID, StuName, Year, GPA)
values(567, 'Theta', 'SO', 4.0);

insert into Student(StuID, StuName, Year, GPA)
values(678, 'Iota', 'FR', 3.8);

insert into Student(StuID, StuName, Year, GPA)
values(789, 'Kappa', 'FR', 3.0);

insert into Course(Subject, Num, Title, Fee)
values('CS', 1234, 'OOP', 80);

insert into Course(Subject, Num, Title, Fee)
values('CS', 2345, 'Compilers', 50);

insert into Course(Subject, Num, Title, Fee)
values('CS', 3456, 'Networks', 100);

insert into Course(Subject, Num, Title, Fee)
values('CS', 4567, 'Databases', 80);

insert into Course(Subject, Num, Title, Fee)
values('MATH', 1234, 'Algebra', 40);

insert into Course(Subject, Num, Title, Fee)
values('MATH', 2345, 'Geometry', 40);

insert into Course(Subject, Num, Title, Fee)
values('MATH', 3456, 'Calculus', 60);

insert into Enroll(StuID, Subject, Num, Grade)
values(123, 'CS', 1234, 'A');

insert into Enroll(StuID, Subject, Num, Grade)
values(123, 'CS', 2345, 'A');

insert into Enroll(StuID, Subject, Num, Grade)
values(123, 'CS', 3456, 'B');

insert into Enroll(StuID, Subject, Num, Grade)
values(234, 'CS', 4567, 'B');

insert into Enroll(StuID, Subject, Num, Grade)
values(234, 'MATH', 1234, 'C');

insert into Enroll(StuID, Subject, Num, Grade)
values(234, 'MATH', 2345, 'C');

insert into Enroll(StuID, Subject, Num, Grade)
values(345, 'MATH', 3456, 'A');

insert into Enroll(StuID, Subject, Num, Grade)
values(345, 'CS', 1234, 'B');

insert into Enroll(StuID, Subject, Num, Grade)
values(456, 'CS', 2345, 'C');

insert into Enroll(StuID, Subject, Num, Grade)
values(456, 'CS', 3456, 'A');

insert into Enroll(StuID, Subject, Num, Grade)
values(567, 'CS', 4567, 'B');

insert into Enroll(StuID, Subject, Num, Grade)
values(567, 'MATH', 1234, 'C');

insert into Enroll(StuID, Subject, Num, Grade)
values(567, 'MATH', 2345, 'A');

insert into Enroll(StuID, Subject, Num, Grade)
values(678, 'MATH', 3456, 'B');

commit;

select * from Student;
select * from Course;
select * from Enroll;