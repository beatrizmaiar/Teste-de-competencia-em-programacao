create database ex2;
use ex2;

CREATE TABLE products (
    id numeric primary key,
    name varchar(255),
    amount numeric,
    price numeric,
    id_categories integer references categories(id)
);

CREATE TABLE categories (
    id numeric primary key,
    name varchar(255)
);

INSERT INTO products (id, name, amount, price, id_categories) VALUES
(1, 'Blue Chair', 30, 300.00, 9),
(2, 'Red Chair', 200, 2150.00, 2),
(3, 'Disney Wardrobe', 400, 829.50, 4),
(4, 'Blue Toaster', 20, 9.90, 3),
(5, 'Solar Panel', 30, 3000.25, 4);

INSERT INTO categories (id, name) VALUES
(1, 'Superior'),
(2, 'Super Luxury'),
(3, 'Modern'),
(4, 'Nerd'),
(5, 'Infantil'),
(6, 'Robust'),
(9, 'Wood');

SELECT p.name, c.name
FROM products p 
JOIN categories c ON  c.id = p.id_categories
WHERE p.amount > 100 AND p.id_categories IN (1, 2, 3, 6, 9)
ORDER BY c.id;