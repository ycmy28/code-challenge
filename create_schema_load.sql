CREATE SCHEMA salary_per_hour
    CREATE TABLE employees (
        employe_id int, 
        branch_id: int, 
        salary int,
        join_date timestamp,
        resign_date timestamp
        )
    CREATE TABLE timesheets (
        timesheet_id int, 
        employee_id: int, 
        dates timestamp,
        checkin timestamp,
        checkout timestamp
        )
    LOAD DATA INFILE 'c:/tmp/employees.csv'
    INTO TABLE employees
    FIELDS TERMINATED BY ','
    IGNORE 1 ROWS;

    LOAD DATA INFILE 'c:/tmp/timesheets.csv'
    INTO TABLE employees
    FIELDS TERMINATED BY ','
    IGNORE 1 ROWS;

    --CREATE VIEW view_salary_per_hour
     --   SELECT * FROM employees;