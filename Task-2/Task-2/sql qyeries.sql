--day 6
-- 1. Create Database

CREATE DATABASE StudentPerformanceDB;


-- 2. Select Database

USE StudentPerformanceDB;


-- 3. Create Table

CREATE TABLE StudentPerformance
(
    StudentID INT PRIMARY KEY,
    Gender VARCHAR(10),
    Department VARCHAR(10),
    Age INT,
    Attendance INT,
    StudyHours INT,
    AssignmentsCompleted INT,
    Marks INT,
    PlacementStatus VARCHAR(20),
    Semester INT
);


-- 4. Import CSV Dataset into Table

BULK INSERT StudentPerformance
FROM 'C:\Users\RAYYAN\Desktop\EDA\dataset\student_performance.csv'
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);


-- 5. Display Imported Data

SELECT * 
FROM StudentPerformance;


--day 7

SELECT StudentID, Gender, Department, Marks
FROM StudentPerformance;

SELECT *
FROM StudentPerformance
WHERE Gender = 'Male';

SELECT *
FROM StudentPerformance
WHERE Gender = 'Female';

SELECT *
FROM StudentPerformance
WHERE Marks > 80;

SELECT *
FROM StudentPerformance
WHERE Marks < 70;

SELECT *
FROM StudentPerformance
WHERE PlacementStatus = 'Placed';

SELECT *
FROM StudentPerformance
WHERE PlacementStatus = 'Not Placed';

SELECT *
FROM StudentPerformance
ORDER BY Marks DESC;

SELECT *
FROM StudentPerformance
ORDER BY Marks ASC;

SELECT TOP 5 *
FROM StudentPerformance
ORDER BY Marks DESC;

SELECT *
FROM StudentPerformance
WHERE Attendance > 90;

SELECT *
FROM StudentPerformance
WHERE StudyHours > 5;

SELECT *
FROM StudentPerformance
WHERE Department = 'IT';

SELECT *
FROM StudentPerformance
WHERE Department = 'CS';

--day8
SELECT COUNT(*) AS Total_Students
FROM StudentPerformance;

SELECT AVG(Marks) AS Average_Marks
FROM StudentPerformance;

SELECT MAX(Marks) AS Highest_Marks
FROM StudentPerformance;

SELECT MIN(Marks) AS Lowest_Marks
FROM StudentPerformance;

SELECT SUM(StudyHours) AS Total_Study_Hours
FROM StudentPerformance;

SELECT Department, COUNT(*) AS Total_Students
FROM StudentPerformance
GROUP BY Department;

SELECT Department, AVG(Marks) AS Average_Marks
FROM StudentPerformance
GROUP BY Department;

SELECT PlacementStatus, COUNT(*) AS Total
FROM StudentPerformance
GROUP BY PlacementStatus;

SELECT Department, AVG(Attendance) AS Average_Attendance
FROM StudentPerformance
GROUP BY Department;

SELECT Department, MAX(Marks) AS Highest_Marks
FROM StudentPerformance
GROUP BY Department;

--day9

SELECT *
FROM StudentPerformance
WHERE PlacementStatus = 'Placed'
AND Marks > 80;

SELECT *
FROM StudentPerformance
WHERE Marks BETWEEN 70 AND 90;

SELECT Department, COUNT(*) AS Total_Students
FROM StudentPerformance
GROUP BY Department;

SELECT PlacementStatus, COUNT(*) AS Total
FROM StudentPerformance
GROUP BY PlacementStatus;

SELECT *
FROM StudentPerformance
WHERE Department = 'IT';

--day 10

CREATE TABLE PlacementDetails
(
    StudentID INT,
    CompanyName VARCHAR(50),
    Package INT,
    PlacementYear INT
);

INSERT INTO PlacementDetails VALUES
(1,'TCS',500000,2025),
(3,'Infosys',600000,2025),
(6,'Wipro',450000,2025),
(10,'Accenture',700000,2025),
(15,'TCS',550000,2025);

SELECT 
StudentPerformance.StudentID,
StudentPerformance.Marks,
PlacementDetails.CompanyName,
PlacementDetails.Package
FROM StudentPerformance
INNER JOIN PlacementDetails
ON StudentPerformance.StudentID = PlacementDetails.StudentID;

SELECT 
StudentPerformance.StudentID,
StudentPerformance.Marks,
PlacementDetails.CompanyName
FROM StudentPerformance
LEFT JOIN PlacementDetails
ON StudentPerformance.StudentID = PlacementDetails.StudentID;

SELECT 
CompanyName,
AVG(Package) AS Average_Package
FROM PlacementDetails
GROUP BY CompanyName;

--day 11
SELECT *
FROM StudentPerformance
WHERE Marks >
(
    SELECT AVG(Marks)
    FROM StudentPerformance
);

SELECT *
FROM StudentPerformance
WHERE Marks =
(
    SELECT MAX(Marks)
    FROM StudentPerformance
);

SELECT *
FROM StudentPerformance
WHERE Attendance >
(
    SELECT AVG(Attendance)
    FROM StudentPerformance
);

SELECT *
FROM StudentPerformance
WHERE PlacementStatus = 'Placed'
AND Marks >
(
    SELECT AVG(Marks)
    FROM StudentPerformance
);

SELECT TOP 1
Department,
AVG(Marks) AS Average_Marks
FROM StudentPerformance
GROUP BY Department
ORDER BY Average_Marks DESC;

