SELECT book.author, SUM(orderdetails.quantity * book.price) AS total_revenue
FROM book
JOIN orderdetails ON book.book_id = orderdetails.book_id
GROUP BY book.author;



#to find book order
SELECT book.title, SUM(orderdetails.quantity) AS total_quantity
FROM book
JOIN orderdetails ON book.book_id = orderdetails.book_id
GROUP BY book.title
HAVING SUM(orderdetails.quantity) > 10;



SELECT Customers.customer_id, Customers.name, SUM(OrderDetails.quantity) AS total_books
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
JOIN OrderDetails ON Orders.order_id = OrderDetails.order_id
WHERE Orders.order_date >= NOW() - INTERVAL 1 YEAR -- Last 1 year
GROUP BY Customers.customer_id, Customers.name
ORDER BY total_books DESC
LIMIT 5;  -- Retrieve top 5 customers