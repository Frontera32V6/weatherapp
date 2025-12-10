select email from employees;
select 
id, first_name, last_name
from employees;
select 
id as employee_id,
email as private_email
from employees;

select distinct first_name
from employees;

select first_name  from employees where first_name = 'Tom';

select count(distinct first_name) as number_of_employees
from employees;

select * from employees	where hire_date > '01.01.2019';

select id, title, min_salary from jobs	where min_salary < 5000;

select * from employees where first_name = "Adam" and last_name = "Irwin";

select * from employees where first_name = "Tom" or first_name = "John";

select * from employees where last_name = "Martinez" or birth_date > '1988-01-01';

select * from employees where not job_id = 3;

select * from employees where department_id = 6 and (job_id = 2 or job_id = 4);

select * from employees where department_id = 3 and not job_id = 2;

select * from jobs order by min_salary desc;

select * from jobs order by min_salary desc, max_salary desc;

select * from jobs where min_salary = 3000 order by max_salary asc;

select * from locations where street_address is null;

select * from employees limit 3;

select * from employees limit 5 offset 10;

select * from employees where department_id = 3 order by hire_date asc limit 5;

alter table employees change COLUMN birth_date oldest_employee datetime;
select * from employees order by oldest_employee asc limit 1;

alter table employees change COLUMN department_id youngest_employee_department_2 int;
select * from employees where youngest_employee_department_2 = 2 order by birth_date desc limit 1;

select first_name, last_name from employees order by hire_date desc limit 1;

select count(department_id) from employee where deperment_id = 2; 
alter table employees change COLUMN department_id number_of_software_engineers int;

------------------------

select * from employees where first_name like "%a"; -- znajdz rekordy, których kolumna first)name konczy sie na 
select * from employees where email like "%gmail.com";
select * from employees where last_name like "__r%"; -- osoby, które mają trzecią litere nazwiska R