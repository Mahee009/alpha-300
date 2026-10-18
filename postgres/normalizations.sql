-- 1NF: every column should have only ONE value , no lists


CREATE TABLE orders_bad(
order_id INT,
customer_name VARCHAR(50),
items VARCHAR(200)
);

INSERT INTO orders_bad VALUES
(1,'Mahee','Dosa, Coffee'),
(2,'Rahul','Biryani');

SELECT * FROM orders_bad;

-- IN 1NF: one item per row
CREATE TABLE orders_1nf(
order_id INT,
customer_name VARCHAR(50),
item VARCHAR(50),
PRIMARY KEY(order_id,item)
);

INSERT INTO orders_1nf VALUES
(1,'Mahee','Dosa'),
(1,'Mahee','Coffee'),
(2,'Rahul','Biryani');

SELECT * FROM orders_1nf;

-- 2NF: must be in 1NF + no partial dependency
-- but item_name and price depend only on item_id (partial dependency)
CREATE TABLE order_items_bad(
order_id INT,
item_id INT,
item_name VARCHAR(50),
price INT,
quantity INT,
PRIMARY KEY(order_id,item_id)
);

-- IN 2NF: move item details to their own table
CREATE TABLE items(
item_id INT PRIMARY KEY,
item_name VARCHAR(50) NOT NULL,
price INT NOT NULL
);

CREATE TABLE order_items(
order_id INT,
item_id INT,
quantity INT NOT NULL,
PRIMARY KEY(order_id,item_id),
FOREIGN KEY(item_id) REFERENCES items(item_id)
);

INSERT INTO items VALUES
(1,'Dosa',60),
(2,'Coffee',30),
(3,'Biryani',150);

INSERT INTO order_items VALUES
(101,1,2),
(101,2,1),
(102,3,1);

SELECT oi.order_id, i.item_name, i.price, oi.quantity
FROM order_items oi
JOIN items i ON oi.item_id = i.item_id;

-- 3NF: must be in 2NF + no transitive dependency
-- non-key column should not depend on another non-key column
-- customer_phone depends on customer_id, not directly on order_id
CREATE TABLE orders_bad(
order_id INT PRIMARY KEY,
customer_id INT,
customer_phone VARCHAR(15),
order_date DATE
);

-- IN 3NF: customer details in a separate table
CREATE TABLE customers(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50) NOT NULL,
customer_phone VARCHAR(15)
);

CREATE TABLE orders(
order_id INT PRIMARY KEY,
customer_id INT NOT NULL,
order_date DATE NOT NULL,
FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES
(1,'Mahee','9876543210'),
(2,'Rahul','9123456780');

INSERT INTO orders VALUES
(101,1,'2026-10-17'),
(102,1,'2026-10-18'),
(103,2,'2026-10-18');

-- phone is stored only once even though name has 2 orders
SELECT o.order_id, c.customer_name, c.customer_phone
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
