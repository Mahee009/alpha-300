
-- Relationships in Postgres
-- 1-to-1, 1-to-many, many-to-many (library example)


-- ---------- 1-to-MANY ----------
-- one author can write many books, but a book has one author

CREATE TABLE authors(
author_id INT PRIMARY KEY,
author_name VARCHAR(50) NOT NULL
);

CREATE TABLE books(
book_id INT PRIMARY KEY,
title VARCHAR(100) NOT NULL,
author_id INT NOT NULL,
FOREIGN KEY(author_id) REFERENCES authors(author_id)
);

INSERT INTO authors VALUES
(1,'R.K. Narayan'),
(2,'Chetan Bhagat');

INSERT INTO books VALUES
(101,'Malgudi Days',1),
(102,'Swami and Friends',1),
(103,'Five Point Someone',2);

-- all books with their author
SELECT b.title, a.author_name
FROM books b
JOIN authors a ON b.author_id = a.author_id;


-- 1-to-1 
-- one member has exactly one membership card
-- UNIQUE on member_id makes it 1-to-1 (otherwise it would be 1-to-many)

CREATE TABLE members(
member_id INT PRIMARY KEY,
member_name VARCHAR(50) NOT NULL
);

CREATE TABLE membership_cards(
card_id INT PRIMARY KEY,
member_id INT NOT NULL UNIQUE,
expiry_date DATE NOT NULL,
FOREIGN KEY(member_id) REFERENCES members(member_id)
);

INSERT INTO members VALUES
(1,'Virinchi'),
(2,'Rahul');

INSERT INTO membership_cards VALUES
(501,1,'2027-06-30'),
(502,2,'2027-12-31');

SELECT m.member_name, c.card_id, c.expiry_date
FROM members m
JOIN membership_cards c ON m.member_id = c.member_id;


--  MANY-to-MANY 
-- one member can borrow many books, one book can be borrowed by many members
-- so we need a junction table (borrows) with a composite primary key

CREATE TABLE borrows(
member_id INT,
book_id INT,
borrow_date DATE NOT NULL,
PRIMARY KEY(member_id,book_id),
FOREIGN KEY(member_id) REFERENCES members(member_id),
FOREIGN KEY(book_id) REFERENCES books(book_id)
);

INSERT INTO borrows VALUES
(1,101,'2026-10-10'),
(1,103,'2026-10-12'),
(2,101,'2026-10-15');

-- which member borrowed which book
SELECT m.member_name, b.title, br.borrow_date
FROM borrows br
JOIN members m ON br.member_id = m.member_id
JOIN books b ON br.book_id = b.book_id;

-- how many books each member borrowed
SELECT m.member_name, COUNT(br.book_id) AS total_borrowed
FROM members m
LEFT JOIN borrows br ON m.member_id = br.member_id
GROUP BY m.member_name;