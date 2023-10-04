SELECT reports.employee_name, manages.employee_name
FROM employees reports
INNER JOIN employees manages
ON reports.manager_id = manages.employee_id;