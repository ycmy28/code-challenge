create table `salary_per_hour` as
SELECT
extract(YEAR FROM order_date) as year, 
extract(MONTH FROM order_date) as month,
branch_id,
employees / (b.checkout * b.checkout) as salary_per_hour 
FROM `employees` as a
join `timesheets` as b
group by b.timesheets,month,year
    
