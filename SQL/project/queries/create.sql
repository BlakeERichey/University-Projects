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