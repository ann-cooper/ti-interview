SELECT customers.name, customers.email, count(orders.customer_id) 
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.id
GROUP BY customer_id
HAVING count(customer_id)>1;