SELECT employee_Name 
FROM emp_salary 
WHERE salary > (SELECT min(salary) FROM emp_salary) AND salary < (SELECT max(salary) FROM emp_salary);