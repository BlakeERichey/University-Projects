DROP TABLE Meetings               CASCADE CONSTRAINTS;
DROP TABLE Donation_Drive_Sponsor CASCADE CONSTRAINTS;
DROP TABLE Org_Donations          CASCADE CONSTRAINTS;
DROP TABLE Team_Sponsor           CASCADE CONSTRAINTS;
DROP TABLE Organization           CASCADE CONSTRAINTS;
DROP TABLE Donor_Donations        CASCADE CONSTRAINTS;
DROP TABLE Donor                  CASCADE CONSTRAINTS;
DROP TABLE Donation_Drive         CASCADE CONSTRAINTS;
DROP TABLE Expenses               CASCADE CONSTRAINTS;
DROP TABLE Works                  CASCADE CONSTRAINTS;
DROP TABLE Cares                  CASCADE CONSTRAINTS;
DROP TABLE Team                   CASCADE CONSTRAINTS;
DROP TABLE Employee               CASCADE CONSTRAINTS;
DROP TABLE Volunteer              CASCADE CONSTRAINTS;
DROP TABLE Needs                  CASCADE CONSTRAINTS;
DROP TABLE Attorney               CASCADE CONSTRAINTS;
DROP TABLE Doctor                 CASCADE CONSTRAINTS;
DROP TABLE Client                 CASCADE CONSTRAINTS;
DROP TABLE Phone_Number           CASCADE CONSTRAINTS;
DROP TABLE Person                 CASCADE CONSTRAINTS;

----------TABLES----------

CREATE TABLE Person(
    id             NUMBER,
    First_Name     VARCHAR2(30 CHAR),
    Middle_Name    VARCHAR2(30 CHAR),
    Last_Name      VARCHAR2(30 CHAR),
    Title          VARCHAR2(30 CHAR),
    DOB            DATE,
    Ethnicity      VARCHAR2(30 CHAR),
    Gender         CHAR(1),
    Profession     VARCHAR2(50 CHAR),
    Email          VARCHAR2(50 CHAR),
    Street_Address VARCHAR2(50 CHAR),
    City           VARCHAR2(30 CHAR),
    State          CHAR(2),
    Zipcode        NUMBER(5),
    Mail_To        CHAR(1),    ---Y/N---
    CHECK      (Mail_To IN('Y', 'N')),
    CONSTRAINT Person_pk PRIMARY KEY(id)
);

CREATE TABLE Phone_Number(
    Person_Id    NUMBER NOT NULL,
    Phone_Number NUMBER NOT NULL,
    Primary      CHAR(1),   ---Y/N---
    Type         VARCHAR2(10 CHAR),
    CHECK       (Primary IN('Y', 'N')),
    FOREIGN KEY(Person_Id) REFERENCES Person(id) on delete cascade,
    CONSTRAINT Phone_Number_pk PRIMARY KEY(Person_Id, Phone_Number)
);

CREATE TABLE Client(
    id                  NUMBER,
    Person_Id           NUMBER UNIQUE,
    Date_Joined         DATE,
    FOREIGN KEY(Person_Id) REFERENCES Person(id) on delete cascade,
    CONSTRAINT Client_pk   PRIMARY KEY(id)
);

CREATE TABLE Doctor(
    Client_Id     NUMBER UNIQUE,
    First_Name    VARCHAR2(50 CHAR),
    Last_Name     VARCHAR2(50 CHAR),
    Doctor_Number NUMBER,
    FOREIGN KEY(Client_Id) REFERENCES Client(id)  on delete cascade
);

CREATE TABLE Attorney(
    Client_Id     NUMBER UNIQUE,
    Attorney_First_Name VARCHAR2(50 CHAR),
    Attorney_Last_Name  VARCHAR2(50 CHAR),
    Attorney_Number     NUMBER,
    FOREIGN KEY(Client_Id) REFERENCES Client(id) on delete cascade
);

CREATE TABLE Needs(
    Client_Id   NUMBER,
    Need        VARCHAR2(30 CHAR),
    Importance  NUMBER(2),
    CHECK(Importance BETWEEN 1 AND 10),
    FOREIGN KEY(Client_Id) REFERENCES Client(id) on delete cascade,
    CONSTRAINT Needs_pk   PRIMARY KEY(Client_Id, Need, Importance)
);

CREATE TABLE Volunteer(
    id             NUMBER,
    Person_Id      NUMBER UNIQUE,
    Date_Joined    DATE,
    FOREIGN KEY(Person_Id)  REFERENCES Person(id) on delete cascade,
    CONSTRAINT Volunteer_pk PRIMARY KEY(id)
);

CREATE TABLE Employee(
    id NUMBER,
    Person_Id       NUMBER,
    Monthly_Salary  NUMBER(6,2),
    Marital_Status  CHAR(1),  ---S, M, D, W
    Job_Title       VARCHAR2(50 CHAR),
    Date_Hired      DATE,
    Type            VARCHAR2(9 CHAR), ---FULL-TIME/PART-TIME
    CHECK (Marital_Status IN('S', 'M', 'D', 'W')),
    CHECK (Type IN('FULL-TIME', 'PART-TIME')),
    FOREIGN KEY(Person_Id) REFERENCES Person(id) on delete cascade,
    CONSTRAINT Employee_pk PRIMARY KEY(id)
);

CREATE TABLE Team(
    Name           VARCHAR2(30 CHAR),
    Type           VARCHAR2(30 CHAR),
    Date_Formed    DATE,
    Team_Leader    NUMBER,
    Reports_To     NUMBER,     ---EMPLOYEE ID
    FOREIGN KEY(Reports_To)  REFERENCES Employee(id) on delete cascade,
    FOREIGN KEY(Team_Leader) REFERENCES Volunteer(ID) on delete cascade,
    CONSTRAINT Team_pk PRIMARY KEY(Name)
);

CREATE TABLE Cares(
    Client_Id    NUMBER,
    Team_Name   VARCHAR2(30 CHAR),
    FOREIGN KEY(Client_Id) REFERENCES Client(id) on delete cascade,
    FOREIGN KEY(Team_Name) REFERENCES Team(Name) on delete cascade,
    CONSTRAINT Cares_pk    PRIMARY KEY(Client_Id, Team_Name)
);

CREATE TABLE Works(
    Volunteer_Id    NUMBER,
    Team_Name       VARCHAR2(30 CHAR),
    Month           CHAR(3),          
    Hours           NUMBER,
    CHECK(MONTH IN('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 
      'SEP', 'OCT', 'NOV', 'DEC')),
    CHECK(HOURS >= 0),
    FOREIGN KEY(Volunteer_Id) REFERENCES Volunteer(id) on delete cascade,
    FOREIGN KEY(Team_Name)    REFERENCES Team(Name) on delete cascade,
    CONSTRAINT Works_pk PRIMARY KEY(Volunteer_Id, Team_Name, Month)
);

CREATE TABLE Expenses(
    Employee_Id NUMBER,
    "Date"  DATE,
    Amount  NUMBER(6, 2),
    Description VARCHAR2(100 CHAR),
    CHECK(Amount > 0),
    FOREIGN KEY(Employee_Id) REFERENCES Employee(id) on delete cascade,
    CONSTRAINT Expenses_pk PRIMARY KEY(Employee_Id, "Date", Amount, Description)
);

CREATE TABLE Donation_Drive(
    Title       VARCHAR2(50 CHAR),
    Employee_Id NUMBER,
    Start_Date  DATE,
    End_Date    DATE,
    Goal        NUMBER(7, 2),
    Theme       VARCHAR2(30 CHAR),
    CHECK(Goal >=0),
    FOREIGN KEY(Employee_Id)     REFERENCES Employee(id) on delete cascade,
    CONSTRAINT Donation_Drive_pk PRIMARY KEY(Title)
);

CREATE TABLE Donor(
    id        NUMBER,
    Person_Id NUMBER,
    FOREIGN KEY(Person_Id) REFERENCES Person(id) on delete cascade,
    CONSTRAINT Donor_pk    PRIMARY KEY(id)
);

CREATE TABLE Donor_Donations(
    id                    NUMBER,
    Donor_id              NUMBER,
    Amount                NUMBER(6, 2),
    Type                  VARCHAR2(10 CHAR),
    Donation_Drive_Title  VARCHAR2(50 CHAR),
    "Date"                DATE,
    Anonymous             CHAR(1), ---Y/N
    CHECK(Amount > 0),
    CHECK(Anonymous IN('Y', 'N')),
    FOREIGN KEY(Donation_Drive_Title) REFERENCES Donation_Drive(Title) on delete cascade,
    FOREIGN KEY(Donor_id) REFERENCES Donor(id) on delete cascade,
    CONSTRAINT Donor_Donations_pk PRIMARY KEY(id)
);

CREATE TABLE Organization(
    Name            VARCHAR2(50 CHAR),
    Person_Id       NUMBER,
    Type            VARCHAR2(50 CHAR),
    Mailing_Address VARCHAR2(75 CHAR),
    Website         VARCHAR2(40 CHAR),
    FOREIGN KEY(Person_Id) REFERENCES Person(id) on delete cascade,
    CONSTRAINT Organization_pk PRIMARY KEY(Name)
);

CREATE TABLE Team_Sponsor(
    Org_Name  VARCHAR2(50 CHAR),
    Team_Name VARCHAR2(30 CHAR),
    FOREIGN KEY(Org_Name)  REFERENCES Organization(Name) on delete cascade,
    FOREIGN KEY(Team_Name) REFERENCES Team(Name) on delete cascade,
    CONSTRAINT Team_Sponsor_pk  PRIMARY KEY(Org_Name, Team_Name)
);

CREATE TABLE Org_Donations(
  id        NUMBER,
  Org_Name  VARCHAR2(50 CHAR),
  Amount    NUMBER(6, 2),
  Type      VARCHAR2(10 CHAR),
  "Date"    DATE,
  Anonymous CHAR(1), ---Y/N
  CHECK(Amount > 0),
  CHECK(Anonymous IN('Y', 'N')),
  FOREIGN KEY(Org_Name)       REFERENCES Organization(Name) on delete cascade,
  CONSTRAINT Org_Donations_pk PRIMARY KEY(id)
);

CREATE TABLE Donation_Drive_Sponsor(
    Title VARCHAR2(50 CHAR),
    Name  VARCHAR2(50 CHAR),
    FOREIGN KEY(Title)      REFERENCES Donation_Drive(Title) on delete cascade,
    FOREIGN KEY(Name)       REFERENCES Organization(Name) on delete cascade,
    CONSTRAINT  Donation_Drive_Sponsor PRIMARY KEY(Title, Name)
);

CREATE TABLE Meetings(
    Employee_Id NUMBER,
    "Date"  DATE,
    Team_Name varchar2(50 char),
    Description VARCHAR2(100 CHAR),
    FOREIGN KEY(Employee_Id) REFERENCES Employee(id) on delete cascade,
    FOREIGN KEY(Team_Name) References team(name) on delete cascade,
    CONSTRAINT meetings_pk PRIMARY KEY(Employee_Id, "Date", Description)
);

--------------INSERTION STATEMENTS---------------

---------INSERT INTO PERSON----------
insert INTO Person(id, First_Name, Middle_Name, Last_Name, Title, DOB, Ethnicity, 
  Gender, Profession, Email, Street_Address, City, State, Zipcode, Mail_To)
VALUES(1, 'Blake', 'Ellis', 'Richey', 'Mr', TO_DATE('03/04/1996', 'MM/DD/YYYY'),
 'White', 'M', 'Software Developer', 'blake.e.richey@gmail.com', 
 '1504 E Lantrip St', 'Kilgore', 'TX', 75662, 'Y');

insert INTO Person(id, First_Name, Middle_Name, Last_Name, Title, DOB, Ethnicity, 
  Gender, Profession, Email, Street_Address, City, State, Zipcode, Mail_To)
VALUES(2, 'James', NULL, 'Kwon', 'Mr', TO_DATE('05/31/1995', 'MM/DD/YYYY'), 
  'Asian', 'M', 'Biomedical Engineer Student', 'james.kwon@gmail.com', 
  '123 Austin St', 'Austin', 'TX', 78708, 'N');

insert INTO Person(id, First_Name, Middle_Name, Last_Name, Title, DOB, Ethnicity, 
  Gender, Profession, Email, Street_Address, City, State, Zipcode, Mail_To)
VALUES(3, 'Kaya', 'Firefly', 'Click', 'Mr', TO_DATE('12/31/1995', 'MM/DD/YYYY'),
 'White', 'M', 'Software Developer', 'kaya.click@gmail.com', '1504 Lantrip', 
 'Kilgore', 'TX', 75662, 'N');

insert INTO Person(id, First_Name, Middle_Name, Last_Name, Title, DOB, Ethnicity, 
  Gender, Profession, Email, Street_Address, City, State, Zipcode, Mail_To)
VALUES(4, 'Tyler', 'Test', 'Andrews', 'Mr', TO_DATE('10/05/1994', 'MM/DD/YYYY'),
 'White', 'M', 'Manifold Fabrication Specialist', 'tyler.andrews@gmail.com', 
 '1504 Lantrip', 'Kilgore', 'TX', 75662, 'N');

insert INTO Person(id, First_Name, Middle_Name, Last_Name, Title, DOB, Ethnicity, 
  Gender, Profession, Email, Street_Address, City, State, Zipcode, Mail_To)
VALUES(5, 'Alpha', 'Beta', 'Delta', 'Miss', TO_DATE('01/02/1994', 'MM/DD/YYYY'),
 'White', 'F', 'Zookeeper', 'abcs@hotmail.com', '165 Prewitt Rd', 'Hallsville', 
 'TX', 75650, 'Y');

insert INTO Person(id, First_Name, Middle_Name, Last_Name, Title, DOB, Ethnicity, 
  Gender, Profession, Email, Street_Address, City, State, Zipcode, Mail_To)
VALUES(6, 'Leonard', 'Lockheart', 'Brown', 'Dr', 
  TO_DATE('06/12/1975', 'MM/DD/YYYY'), 'African American', 'M', 
  'Computer Science Professor', 'lbrown@uttyler.edu', '3000 University Blvd', 
  'Tyler', 'TX', 75701, 'Y');

insert INTO Person(id, First_Name, Middle_Name, Last_Name, Title, DOB, Ethnicity, 
  Gender, Profession, Email, Street_Address, City, State, Zipcode, Mail_To)
VALUES(7, 'Geralt', 'Witcher', 'Rivia', 'Mr', 
  TO_DATE('08/04/1909', 'MM/DD/YYYY'), 'White', 'M', 'Witcher', 
  'cdprojectred@gamers.net', '300 W Rivia', 'Poland', 'TX', 77710, 'Y');

insert INTO Person(id, First_Name, Middle_Name, Last_Name, Title, DOB, Ethnicity, 
  Gender, Profession, Email, Street_Address, City, State, Zipcode, Mail_To)
VALUES(8, 'Walluam', 'Esper', 'Bard', 'Mr', TO_DATE('03/20/2019', 'MM/DD/YYYY'),
 'White', 'M', 'Musician', 'deseuler@yahoo.com', '230 Cotton St', 'Longview', 
 'TX', 75601, 'Y');

insert INTO Person(id, First_Name, Middle_Name, Last_Name, Title, DOB, Ethnicity, 
  Gender, Profession, Email, Street_Address, City, State, Zipcode, Mail_To)
VALUES(9, 'Atleetaleetalee', NULL, NULL, 'Mr', 
  TO_DATE('05/21/2018', 'MM/DD/YYYY'), 'Blue', 'M', 'Military General', 
  'deseuler@gmail.com', '9 Tulas Ave', 'Aklar', 'TX', 79835, 'Y');

insert INTO Person(id, First_Name, Middle_Name, Last_Name, Title, DOB, Ethnicity, 
  Gender, Profession, Email, Street_Address, City, State, Zipcode, Mail_To)
VALUES(10, 'Reginald', 'Archibald', 'Qralorae', 'Mr', 
  TO_DATE('06/09/2017', 'MM/DD/YYYY'), 'White', 'M', 'Historian', 
  'blake.e.richey@gmail.com', '777 Nihon Court', 'Norwegistania', 'TX', 75000, 
  'Y');

----------INSERT INTO PHONE NUMBER----------

insert INTO Phone_Number(Person_Id, Phone_Number, Primary, Type)
VALUES           (1, 9033538260, 'Y', 'Cell');

insert INTO Phone_Number(Person_Id, Phone_Number, Primary, Type)
VALUES           (1, 9033536496, 'N', 'Cell');

insert INTO Phone_Number(Person_Id, Phone_Number, Primary, Type)
VALUES           (2, 5128797342, 'Y', 'Cell');

insert INTO Phone_Number(Person_Id, Phone_Number, Primary, Type)
VALUES           (3, 9032522207, 'Y', 'Cell');

insert INTO Phone_Number(Person_Id, Phone_Number, Primary, Type)
VALUES           (4, 9034318514, 'Y', 'Cell');

insert INTO Phone_Number(Person_Id, Phone_Number, Primary, Type)
VALUES           (4, 9033538260, 'N', 'Cell');

insert INTO Phone_Number(Person_Id, Phone_Number, Primary, Type)
VALUES           (5, 1112223333, 'Y', 'Home');

insert INTO Phone_Number(Person_Id, Phone_Number, Primary, Type)
VALUES           (6, 9035715703, 'Y', 'Business');

insert INTO Phone_Number(Person_Id, Phone_Number, Primary, Type)
VALUES           (8, 9035551234, 'Y', 'Home');

insert INTO Phone_Number(Person_Id, Phone_Number, Primary, Type)
VALUES           (10, 9035557777, 'Y', 'Cell');


----------INSERT INTO CLIENT----------

insert INTO Client(id, Person_Id, Date_Joined) VALUES(1,  1,  TO_DATE('01/01/2018', 'MM/DD/YYYY'));
insert INTO Client(id, Person_Id, Date_Joined) VALUES(2,  2,  TO_DATE('02/06/2018', 'MM/DD/YYYY'));
insert INTO Client(id, Person_Id, Date_Joined) VALUES(3,  4,  TO_DATE('03/09/2018', 'MM/DD/YYYY'));
insert INTO Client(id, Person_Id, Date_Joined) VALUES(4,  6,  TO_DATE('04/19/2018', 'MM/DD/YYYY'));
insert INTO Client(id, Person_Id, Date_Joined) VALUES(5,  8,  TO_DATE('05/23/2018', 'MM/DD/YYYY'));
insert INTO Client(id, Person_Id, Date_Joined) VALUES(6,  10, TO_DATE('06/12/2018', 'MM/DD/YYYY'));
insert INTO Client(id, Person_Id, Date_Joined) VALUES(7,  3,  TO_DATE('07/17/2018', 'MM/DD/YYYY'));
insert INTO Client(id, Person_Id, Date_Joined) VALUES(8,  5,  TO_DATE('08/10/2018', 'MM/DD/YYYY'));
insert INTO Client(id, Person_Id, Date_Joined) VALUES(9,  7,  TO_DATE('09/03/2018', 'MM/DD/YYYY'));
insert INTO Client(id, Person_Id, Date_Joined) VALUES(10, 9,  TO_DATE('09/30/2018', 'MM/DD/YYYY'));


----------INSERT INTO DOCTOR----------

insert INTO Doctor(Client_Id, First_Name, Last_Name, Doctor_Number) 
VALUES     (1,  'Matt',   'Hipke',    9033337898);
insert INTO Doctor(Client_Id, First_Name, Last_Name, Doctor_Number) 
VALUES     (2,  'Aaron',  'Smith',    4137585685);
insert INTO Doctor(Client_Id, First_Name, Last_Name, Doctor_Number) 
VALUES     (3,  'Abdul',  'Johnson',  8318200627);
insert INTO Doctor(Client_Id, First_Name, Last_Name, Doctor_Number) 
VALUES     (4,  'Abe',    'Williams', 5225692491);
insert INTO Doctor(Client_Id, First_Name, Last_Name, Doctor_Number) 
VALUES     (5,  'Alex',   'Jones',    3043153218);
insert INTO Doctor(Client_Id, First_Name, Last_Name, Doctor_Number) 
VALUES     (6,  'John',   'Brown',    6494678524);
insert INTO Doctor(Client_Id, First_Name, Last_Name, Doctor_Number) 
VALUES     (7,  'James',  'Davis',    3954291377);
insert INTO Doctor(Client_Id, First_Name, Last_Name, Doctor_Number) 
VALUES     (8,  'Brent',  'Miller',   9056628259);
insert INTO Doctor(Client_Id, First_Name, Last_Name, Doctor_Number) 
VALUES     (9,  'Lloyd',  'Wilson',   2757367132);
insert INTO Doctor(Client_Id, First_Name, Last_Name, Doctor_Number) 
VALUES     (10, 'Amanda', 'Robinson', 9572180473);


----------INSERT INTO ATTORNEY----------

insert INTO Attorney(Client_Id, Attorney_First_Name, Attorney_Last_Name, Attorney_Number) 
VALUES       (1,  'Patrick',  'Chan',       8354992912);
insert INTO Attorney(Client_Id, Attorney_First_Name, Attorney_Last_Name, Attorney_Number) 
VALUES       (2,  'Oswaldo',  'Villa',      9648542765);
insert INTO Attorney(Client_Id, Attorney_First_Name, Attorney_Last_Name, Attorney_Number) 
VALUES       (3,  'Patricia', 'Avila',      3486902027);
insert INTO Attorney(Client_Id, Attorney_First_Name, Attorney_Last_Name, Attorney_Number) 
VALUES       (4,  'Paris',    'Fernandez',  5273444119);
insert INTO Attorney(Client_Id, Attorney_First_Name, Attorney_Last_Name, Attorney_Number) 
VALUES       (5,  'Scott',    'Strickland', 3552067122);
insert INTO Attorney(Client_Id, Attorney_First_Name, Attorney_Last_Name, Attorney_Number) 
VALUES       (6,  'Seth',     'Velez',      6666432755);
insert INTO Attorney(Client_Id, Attorney_First_Name, Attorney_Last_Name, Attorney_Number) 
VALUES       (7,  'Trey',     'Sellers',    7845123652);
insert INTO Attorney(Client_Id, Attorney_First_Name, Attorney_Last_Name, Attorney_Number) 
VALUES       (8,  'Wayne',    'Herman',     3642897099);
insert INTO Attorney(Client_Id, Attorney_First_Name, Attorney_Last_Name, Attorney_Number) 
VALUES       (9,  'Emily',    'Warner',     2244391860);
insert INTO Attorney(Client_Id, Attorney_First_Name, Attorney_Last_Name, Attorney_Number) 
VALUES       (10, 'Susan',    'Anthony',    9549279451);

----------INSERT INTO NEEDS----------

insert INTO Needs(Client_Id, Need, Importance) VALUES(1,  'Housekeeping',    6);
insert INTO Needs(Client_Id, Need, Importance) VALUES(1,  'Transportation',  1);
insert INTO Needs(Client_Id, Need, Importance) VALUES(2,  'Shopping',        6);
insert INTO Needs(Client_Id, Need, Importance) VALUES(2,  'Cooking',         4);
insert INTO Needs(Client_Id, Need, Importance) VALUES(3,  'Shopping',        7);
insert INTO Needs(Client_Id, Need, Importance) VALUES(5,  'Yard Work',       8);
insert INTO Needs(Client_Id, Need, Importance) VALUES(6,  'Housekeeping',    2);
insert INTO Needs(Client_Id, Need, Importance) VALUES(7,  'Yard Work',       3);
insert INTO Needs(Client_Id, Need, Importance) VALUES(9,  'Transportation', 10);
insert INTO Needs(Client_Id, Need, Importance) VALUES(10, 'Shopping',        5);


----------INSERT INTO VOLUNTEER----------

insert INTO Volunteer(id, Person_Id, Date_Joined) 
VALUES        (1,  1,  TO_DATE('04/19/2019', 'MM/DD/YYYY'));
insert INTO Volunteer(id, Person_Id, Date_Joined) 
VALUES        (2,  10, TO_DATE('01/02/2003', 'MM/DD/YYYY'));
insert INTO Volunteer(id, Person_Id, Date_Joined) 
VALUES        (3,  9,  TO_DATE('10/13/2001', 'MM/DD/YYYY'));
insert INTO Volunteer(id, Person_Id, Date_Joined) 
VALUES        (4,  2,  TO_DATE('06/07/2011', 'MM/DD/YYYY'));
insert INTO Volunteer(id, Person_Id, Date_Joined)
VALUES        (5,  8,  TO_DATE('07/23/2006', 'MM/DD/YYYY'));
insert INTO Volunteer(id, Person_Id, Date_Joined) 
VALUES        (6,  3,  TO_DATE('03/14/2009', 'MM/DD/YYYY'));
insert INTO Volunteer(id, Person_Id, Date_Joined) 
VALUES        (7,  7,  TO_DATE('01/17/2007', 'MM/DD/YYYY'));
insert INTO Volunteer(id, Person_Id, Date_Joined) 
VALUES        (8,  4,  TO_DATE('09/12/2016', 'MM/DD/YYYY'));
insert INTO Volunteer(id, Person_Id, Date_Joined) 
VALUES        (9,  6,  TO_DATE('08/29/2017', 'MM/DD/YYYY'));
insert INTO Volunteer(id, Person_Id, Date_Joined) 
VALUES        (10, 5,  TO_DATE('11/30/2018', 'MM/DD/YYYY'));


----------INSERT INTO EMPLOYEE----------

INSERT INTO Employee(id, Person_Id, Monthly_Salary, Marital_Status, Job_Title, Date_Hired, Type) 
VALUES       (1,  1,  1200.00, 'S', (SELECT Profession FROM Person WHERE Person.id =  1), 
  TO_DATE('01/02/2018', 'MM/DD/YYYY'), 'PART-TIME');
INSERT INTO Employee(id, Person_Id, Monthly_Salary, Marital_Status, Job_Title, Date_Hired, Type) 
VALUES       (2,  2,   300.00, 'S', (SELECT Profession FROM Person WHERE Person.id =  2), 
  TO_DATE('05/09/2017', 'MM/DD/YYYY'), 'FULL-TIME');
INSERT INTO Employee(id, Person_Id, Monthly_Salary, Marital_Status, Job_Title, Date_Hired, Type) 
VALUES       (3,  3,  3000.00, 'S', (SELECT Profession FROM Person WHERE Person.id =  3), 
  TO_DATE('08/06/2015', 'MM/DD/YYYY'), 'FULL-TIME');
INSERT INTO Employee(id, Person_Id, Monthly_Salary, Marital_Status, Job_Title, Date_Hired, Type) 
VALUES       (4,  4,  2000.00, 'S', (SELECT Profession FROM Person WHERE Person.id =  4), 
  TO_DATE('09/23/2013', 'MM/DD/YYYY'), 'PART-TIME');
INSERT INTO Employee(id, Person_Id, Monthly_Salary, Marital_Status, Job_Title, Date_Hired, Type) 
VALUES       (5,  5,  1100.00, 'W', (SELECT Profession FROM Person WHERE Person.id =  5), 
  TO_DATE('02/21/2008', 'MM/DD/YYYY'), 'FULL-TIME');
INSERT INTO Employee(id, Person_Id, Monthly_Salary, Marital_Status, Job_Title, Date_Hired, Type) 
VALUES       (6,  6,  2500.00, 'M', (SELECT Profession FROM Person WHERE Person.id =  6), 
  TO_DATE('06/19/2009', 'MM/DD/YYYY'), 'FULL-TIME');
INSERT INTO Employee(id, Person_Id, Monthly_Salary, Marital_Status, Job_Title, Date_Hired, Type) 
VALUES       (7,  7,  1000.00, 'S', (SELECT Profession FROM Person WHERE Person.id =  7), 
  TO_DATE('11/14/2009', 'MM/DD/YYYY'), 'FULL-TIME');
INSERT INTO Employee(id, Person_Id, Monthly_Salary, Marital_Status, Job_Title, Date_Hired, Type) 
VALUES       (8,  8,   900.00, 'D', (SELECT Profession FROM Person WHERE Person.id =  8), 
  TO_DATE('12/11/2008', 'MM/DD/YYYY'), 'PART-TIME');
INSERT INTO Employee(id, Person_Id, Monthly_Salary, Marital_Status, Job_Title, Date_Hired, Type) 
VALUES       (9,  9,  4000.00, 'S', (SELECT Profession FROM Person WHERE Person.id =  9), 
  TO_DATE('07/30/2011', 'MM/DD/YYYY'), 'FULL-TIME');
INSERT INTO Employee(id, Person_Id, Monthly_Salary, Marital_Status, Job_Title, Date_Hired, Type) 
VALUES       (10, 10, 1900.00, 'M', (SELECT Profession FROM Person WHERE Person.id = 10), 
  TO_DATE('02/08/2010', 'MM/DD/YYYY'), 'PART-TIME');

----------INSERT INTO TEAM----------

INSERT INTO Team(Name, Type, Date_Formed, Team_Leader, Reports_To) 
VALUES   ('ICPC',                  'Extracurricular', 
  TO_DATE('04/20/2010', 'MM/DD/YYYY'),  3,    5);
INSERT INTO Team(Name, Type, Date_Formed, Team_Leader, Reports_To) 
VALUES   ('IEEE Robotics',        'Extracurricular',  
  TO_DATE('01/01/2019', 'MM/DD/YYYY'),  1,    2);
INSERT INTO Team(Name, Type, Date_Formed, Team_Leader, Reports_To) 
VALUES   ('DND',                  'Fun and Games',    
  TO_DATE('04/20/2010', 'MM/DD/YYYY'),  4,    1);
INSERT INTO Team(Name, Type, Date_Formed, Team_Leader, Reports_To) 
VALUES   ('ATMAE',                'Organizational',   
  TO_DATE('04/20/2010', 'MM/DD/YYYY'),  2,    3);
INSERT INTO Team(Name, Type, Date_Formed, Team_Leader, Reports_To) 
VALUES   ('SHRM',                 'Networking',       
  TO_DATE('04/20/2010', 'MM/DD/YYYY'),  5,    6);
INSERT INTO Team(Name, Type, Date_Formed, Team_Leader, Reports_To) 
VALUES   ('Painters Club',        'Civil Service',    
  TO_DATE('04/20/2010', 'MM/DD/YYYY'),  6,    4);
INSERT INTO Team(Name, Type, Date_Formed, Team_Leader, Reports_To) 
VALUES   ('Trinity Givers',       'Religious',        
  TO_DATE('04/20/2010', 'MM/DD/YYYY'),  9,    9);
INSERT INTO Team(Name, Type, Date_Formed, Team_Leader, Reports_To) 
VALUES   ('UIL',                  'Extracurricular',  
  TO_DATE('04/20/2010', 'MM/DD/YYYY'),  7,    8);
INSERT INTO Team(Name, Type, Date_Formed, Team_Leader, Reports_To) 
VALUES   ('Speling tha rite way', 'Competitive',      
  TO_DATE('04/20/2010', 'MM/DD/YYYY'), 10,    7);
INSERT INTO Team(Name, Type, Date_Formed, Team_Leader, Reports_To) 
VALUES   ('Cant Touch This',      'Dance',            
  TO_DATE('04/20/2010', 'MM/DD/YYYY'),  8,   10);


----------INSERT INTO CARES----------

insert INTO Cares(Client_Id, Team_Name) VALUES(1, 'DND'                 );
insert INTO Cares(Client_Id, Team_Name) VALUES(2, 'Painters Club'       );
insert INTO Cares(Client_Id, Team_Name) VALUES(3, 'SHRM'                );
insert INTO Cares(Client_Id, Team_Name) VALUES(4, 'Trinity Givers'      );
insert INTO Cares(Client_Id, Team_Name) VALUES(5, 'Trinity Givers'      );
insert INTO Cares(Client_Id, Team_Name) VALUES(6, 'ICPC'                );
insert INTO Cares(Client_Id, Team_Name) VALUES(7, 'Cant Touch This'     );
insert INTO Cares(Client_Id, Team_Name) VALUES(8, 'Trinity Givers'      );
insert INTO Cares(Client_Id, Team_Name) VALUES(9, 'Speling tha rite way');
insert INTO Cares(Client_Id, Team_Name) VALUES(10, 'ATMAE'              );

----------INSERT INTO WORKS----------

insert INTO Works(Volunteer_Id, Team_Name, Month, Hours) VALUES(10, 'DND'                 , 'JAN', 30);
insert INTO Works(Volunteer_Id, Team_Name, Month, Hours) VALUES( 9, 'Painters Club'       , 'MAR', 15);
insert INTO Works(Volunteer_Id, Team_Name, Month, Hours) VALUES( 8, 'SHRM'                , 'JUN', 20);
insert INTO Works(Volunteer_Id, Team_Name, Month, Hours) VALUES( 7, 'Trinity Givers'      , 'MAR', 44);
insert INTO Works(Volunteer_Id, Team_Name, Month, Hours) VALUES( 6, 'Trinity Givers'      , 'JUL', 19);
insert INTO Works(Volunteer_Id, Team_Name, Month, Hours) VALUES( 5, 'ICPC'                , 'MAR', 32);
insert INTO Works(Volunteer_Id, Team_Name, Month, Hours) VALUES( 4, 'Cant Touch This'     , 'DEC', 36);
insert INTO Works(Volunteer_Id, Team_Name, Month, Hours) VALUES( 3, 'Trinity Givers'      , 'JAN', 19);
insert INTO Works(Volunteer_Id, Team_Name, Month, Hours) VALUES( 2, 'Speling tha rite way', 'MAR', 18);
insert INTO Works(Volunteer_Id, Team_Name, Month, Hours) VALUES( 1, 'ATMAE'               , 'OCT', 29);

---------INSERT INTO DONOR ----------
INSERT INTO Donor(id,Person_Id) values(1,1);
INSERT INTO Donor(id,Person_Id) values(2,3);
INSERT INTO Donor(id,Person_Id) values(3,5);
INSERT INTO Donor(id,Person_Id) values(4,5);
INSERT INTO Donor(id,Person_Id) values(5,7);
INSERT INTO Donor(id,Person_Id) values(6,9);
INSERT INTO Donor(id,Person_Id) values(7,10);
INSERT INTO Donor(id,Person_Id) values(8,5);
INSERT INTO Donor(id,Person_Id) values(9,9);
INSERT INTO Donor(id,Person_Id) values(10,3);

-------insert into donation_drive------------
insert into Donation_Drive(title,employee_id,start_date,end_date,goal,theme) values('donation_drive1',1,TO_DATE('03/25/2010','MM/DD/YYYY'),TO_DATE('03/26/2010','MM-DD-YYYY'),1000,'star wars');
insert into Donation_Drive(title,employee_id,start_date,end_date,goal,theme) values('donation_drive2',2,TO_DATE('04/15/2017','MM/DD/YYYY'),TO_DATE('04/16/2017','MM/DD/YYYY'),500,'lord of the rings');
insert into Donation_Drive(title,employee_id,start_date,end_date,goal,theme) values('donation_drive3',3,TO_DATE('03/28/2018','MM/DD/YYYY'),TO_DATE('04/01/2018','MM/DD/YYYY'),1500,'harry potter');
insert into Donation_Drive(title,employee_id,start_date,end_date,goal,theme) values('donation_drive4',3,TO_DATE('08/21/2016','MM/DD/YYYY'),TO_DATE('08/22/2016','MM/DD/YYYY'),100,'sql party');
insert into Donation_Drive(title,employee_id,start_date,end_date,goal,theme) values('donation_drive5',1,TO_DATE('07/11/2014','MM/DD/YYYY'),TO_DATE('07/12/2014','MM/DD/YYYY'),6000,'do my laundry drive');
insert into Donation_Drive(title,employee_id,start_date,end_date,goal,theme) values('donation_drive6',6,TO_DATE('11/12/2013','MM/DD/YYYY'),TO_DATE('11/13/2013','MM/DD/YYYY'),5000,'military');
insert into Donation_Drive(title,employee_id,start_date,end_date,goal,theme) values('donation_drive7',8,TO_DATE('03/25/2012','MM/DD/YYYY'),TO_DATE('03/26/2012','MM/DD/YYYY'),8000,'warcraft');
insert into Donation_Drive(title,employee_id,start_date,end_date,goal,theme) values('donation_drive8',1,TO_DATE('09/14/2019','MM/DD/YYYY'),TO_DATE('09/15/2019','MM/DD/YYYY'),4000,'starcraft');
insert into Donation_Drive(title,employee_id,start_date,end_date,goal,theme) values('donation_drive9',9,TO_DATE('06/09/2018','MM/DD/YYYY'),TO_DATE('06/10/2018','MM/DD/YYYY'),10000,'fortnite');
insert into Donation_Drive(title,employee_id,start_date,end_date,goal,theme) values('donation_drive10',10,TO_DATE('12/20/2020','MM/DD/YYYY'),TO_DATE('12/21/2020','MM/DD/YYYY'),9000,'summer');

-------- insert into donor_donations

insert into Donor_Donations(id,donor_id,amount,type,donation_drive_title,"Date",Anonymous) values(1,1,500,'check',null,TO_DATE('03/25/2010','MM-DD-YYYY'),'Y');
insert into Donor_Donations(id,donor_id,amount,type,donation_drive_title,"Date",Anonymous) values(2,1,100,'credit','donation_drive1',TO_DATE('10/19/2016','MM-DD-YYYY'),'Y');
insert into Donor_Donations(id,donor_id,amount,type,donation_drive_title,"Date",Anonymous) values(3,2,600,'debit',null,TO_DATE('03/25/2010','MM-DD-YYYY'),'N');
insert into Donor_Donations(id,donor_id,amount,type,donation_drive_title,"Date",Anonymous) values(4,5,900,'cash','donation_drive2',TO_DATE('08/21/2014','MM-DD-YYYY'),'Y');
insert into Donor_Donations(id,donor_id,amount,type,donation_drive_title,"Date",Anonymous) values(5,7,5,'credit',null,TO_DATE('09/25/2010','MM-DD-YYYY'),'N');
insert into Donor_Donations(id,donor_id,amount,type,donation_drive_title,"Date",Anonymous) values(6,6,22,'check','donation_drive3',TO_DATE('08/22/1988','MM-DD-YYYY'),'N');
insert into Donor_Donations(id,donor_id,amount,type,donation_drive_title,"Date",Anonymous) values(7,4,300,'debit',null,TO_DATE('2/23/2002','MM-DD-YYYY'),'N');
insert into Donor_Donations(id,donor_id,amount,type,donation_drive_title,"Date",Anonymous) values(8,10,150,'credit','donation_drive4',TO_DATE('07/12/2015','MM-DD-YYYY'),'Y');
insert into Donor_Donations(id,donor_id,amount,type,donation_drive_title,"Date",Anonymous) values(9,6,777,'cash',null,TO_DATE('06/14/2019','MM-DD-YYYY'),'N');
insert into Donor_Donations(id,donor_id,amount,type,donation_drive_title,"Date",Anonymous) values(10,8,666,'cash','donation_drive5',TO_DATE('08/10/1699','MM-DD-YYYY'),'Y');


------- insert into organization ------------------

insert into Organization(name,person_id,type,mailing_address,website) values('organization1',1,'for-profit','123 drive way','wwww.organization.com');
insert into Organization(name,person_id,type,mailing_address,website) values('organization2',2,'for-profit','456 park place','wwww.organization2.com');
insert into Organization(name,person_id,type,mailing_address,website) values('organization3',3,'for-profit','789 drive drive','wwww.organization3.com');
insert into Organization(name,person_id,type,mailing_address,website) values('organization4',4,'non-profit','555 university way','wwww.organization4.com');
insert into Organization(name,person_id,type,mailing_address,website) values('organization5',5,'non-profit','123 roundaboutway','wwww.organization5.com');
insert into Organization(name,person_id,type,mailing_address,website) values('organization6',6,'non-profit','666 depths below','wwww.organization6.com');
insert into Organization(name,person_id,type,mailing_address,website) values('organization7',7,'non-profit','123 fourfivesix','wwww.organization7.com');
insert into Organization(name,person_id,type,mailing_address,website) values('organization8',8,'non-profit','999 altered six','wwww.organization8.com');
insert into Organization(name,person_id,type,mailing_address,website) values('organization9',9,'for-profit','558 south park blvd','wwww.organization9.com');
insert into Organization(name,person_id,type,mailing_address,website) values('organization10',10,'non-profit','301 north park blvd','wwww.organization10.com');


--- insert into organization donations ----

insert into Org_Donations (id,Org_Name,Amount,Type,"Date",Anonymous) values(1,'organization1',500,'debit',TO_DATE('08/21/2018','MM-DD-YYYY'),'Y');
insert into Org_Donations (id,Org_Name,Amount,Type,"Date",Anonymous) values(2,'organization2',5000,'credit',TO_DATE('09/22/2020','MM-DD-YYYY'),'N');
insert into Org_Donations (id,Org_Name,Amount,Type,"Date",Anonymous) values(3,'organization3',880,'debit',TO_DATE('10/01/2014','MM-DD-YYYY'),'N');
insert into Org_Donations (id,Org_Name,Amount,Type,"Date",Anonymous) values(4,'organization3',9000,'credit',TO_DATE('11/15/2006','MM-DD-YYYY'),'N');
insert into Org_Donations (id,Org_Name,Amount,Type,"Date",Anonymous) values(5,'organization5',450,'check',TO_DATE('06/13/2008','MM-DD-YYYY'),'N');
insert into Org_Donations (id,Org_Name,Amount,Type,"Date",Anonymous) values(6,'organization9',666,'check',TO_DATE('07/14/2015','MM-DD-YYYY'),'Y');
insert into Org_Donations (id,Org_Name,Amount,Type,"Date",Anonymous) values(7,'organization10',123,'check',TO_DATE('09/06/2014','MM-DD-YYYY'),'Y');
insert into Org_Donations (id,Org_Name,Amount,Type,"Date",Anonymous) values(8,'organization2',999,'debit',TO_DATE('04/11/2017','MM-DD-YYYY'),'Y');
insert into Org_Donations (id,Org_Name,Amount,Type,"Date",Anonymous) values(9,'organization4',1500,'credit',TO_DATE('06/15/1970','MM-DD-YYYY'),'Y');
insert into Org_Donations (id,Org_Name,Amount,Type,"Date",Anonymous) values(10,'organization1',2300,'check',TO_DATE('05/01/2005','MM-DD-YYYY'),'N');


-- insert into expenses --
insert into Expenses(employee_id,"Date",amount,description) values (1,TO_DATE('06/25/2018','MM-DD-YYYY'),500,'gas for trip');
insert into Expenses(employee_id,"Date",amount,description) values (1,TO_DATE('06/25/2018','MM-DD-YYYY'),100,'warcraft subscription');
insert into Expenses(employee_id,"Date",amount,description) values (2,TO_DATE('06/25/2018','MM-DD-YYYY'),45,'league is 100% free');
insert into Expenses(employee_id,"Date",amount,description) values (5,TO_DATE('06/25/2018','MM-DD-YYYY'),55,'steam sale');
insert into Expenses(employee_id,"Date",amount,description) values (6,TO_DATE('06/25/2018','MM-DD-YYYY'),60,'necessary accessories');
insert into Expenses(employee_id,"Date",amount,description) values (10,TO_DATE('06/25/2018','MM-DD-YYYY'),80,'groceries');
insert into Expenses(employee_id,"Date",amount,description) values (8,TO_DATE('06/25/2018','MM-DD-YYYY'),50,'dinner out');
insert into Expenses(employee_id,"Date",amount,description) values (9,TO_DATE('06/25/2018','MM-DD-YYYY'),60,'necessary vidya game');
insert into Expenses(employee_id,"Date",amount,description) values (4,TO_DATE('06/25/2018','MM-DD-YYYY'),80,'cell phone');
insert into Expenses(employee_id,"Date",amount,description) values (6,TO_DATE('06/25/2018','MM-DD-YYYY'),10,'taco bell');

----insert into donation_drive_sponsor-------
insert into Donation_Drive_Sponsor(title,name) values('donation_drive1','organization2');
insert into Donation_Drive_Sponsor(title,name) values('donation_drive10','organization8');
insert into Donation_Drive_Sponsor(title,name) values('donation_drive4','organization1');
insert into Donation_Drive_Sponsor(title,name) values('donation_drive4','organization3');
insert into Donation_Drive_Sponsor(title,name) values('donation_drive5','organization5');
insert into Donation_Drive_Sponsor(title,name) values('donation_drive3','organization6');
insert into Donation_Drive_Sponsor(title,name) values('donation_drive1','organization7');
insert into Donation_Drive_Sponsor(title,name) values('donation_drive9','organization3');
insert into Donation_Drive_Sponsor(title,name) values('donation_drive4','organization4');
insert into Donation_Drive_Sponsor(title,name) values('donation_drive1','organization6');

--insert into meetings---
insert into Meetings(Employee_id,"Date",Team_Name,Description) values(1,TO_DATE('06/20/2018','MM-DD-YYYY'),'Cant Touch This','Very hot at meeting');
insert into Meetings(Employee_id,"Date",Team_Name,Description) values(2,TO_DATE('06/15/2018','MM-DD-YYYY'),'Cant Touch This','Very cold at meeting');
insert into Meetings(Employee_id,"Date",Team_Name,Description) values(3,TO_DATE('06/14/2018','MM-DD-YYYY'),'Cant Touch This','Very mild at meeting');
insert into Meetings(Employee_id,"Date",Team_Name,Description) values(8,TO_DATE('06/13/2018','MM-DD-YYYY'),'Cant Touch This','Very not-hot at meeting');
insert into Meetings(Employee_id,"Date",Team_Name,Description) values(1,TO_DATE('06/10/2018','MM-DD-YYYY'),'Cant Touch This','Very not-cold at meeting');
insert into Meetings(Employee_id,"Date",Team_Name,Description) values(5,TO_DATE('06/08/2018','MM-DD-YYYY'),'Cant Touch This','Very not not-cold at meeting');
insert into Meetings(Employee_id,"Date",Team_Name,Description) values(9,TO_DATE('06/01/2018','MM-DD-YYYY'),'Cant Touch This','Very not not-hot at meeting');
insert into Meetings(Employee_id,"Date",Team_Name,Description) values(10,TO_DATE('05/25/2018','MM-DD-YYYY'),'Cant Touch This','Very not mild at meeting');
insert into Meetings(Employee_id,"Date",Team_Name,Description) values(4,TO_DATE('05/10/2018','MM-DD-YYYY'),'Cant Touch This','Very not not-mild at meeting');
insert into Meetings(Employee_id,"Date",Team_Name,Description) values(6,TO_DATE('05/08/2018','MM-DD-YYYY'),'Cant Touch This','MEETING COLLAPSED INTO THE VOID');


----------SELECT STATEMENTS----------
--SELECT * FROM Person;
--SELECT * FROM Phone_Number;
--SELECT * FROM Client;
--SELECT * FROM Doctor;
--SELECT * FROM Attorney;
--SELECT * FROM Needs;
--SELECT * FROM Volunteer;
--SELECT * FROM Employee;
--SELECT * FROM Team;
--SELECT * FROM Cares;
--SELECT * FROM Works;
--SELECT * FROM Expenses;
--SELECT * FROM Donor;
--SELECT * FROM Donor_Donations;
--SELECT * FROM Organization;
--SELECT * FROM Team_Sponsor;
--SELECT * FROM Org_Donations;
--SELECT * FROM Donation_Drive;
--SELECT * FROM Donation_Drive_Sponsor;
--select * from Meetings;