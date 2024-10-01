CREATE DATABASE ex3;
USE ex3;

CREATE TABLE products (
    id int primary key,
    name varchar(255),
    amount numeric,
    price numeric,
    id_categories integer references categories(id)
);

CREATE TABLE categories (
    id int primary key,
    name varchar(255)
);

INSERT INTO products (id, name, amount, price, id_categories) VALUES
(1, 'Two-doors wardrobe', 100, 800, 1),
(2, 'Dining table', 1000, 560, 3),
(3, 'Towel holder', 10000, 25.50, 4),
(4, 'Computer desk', 350, 320.50, 2),
(5, 'Chair', 3000, 210.64, 4),
(6, 'Single bed', 750, 460, 1);

INSERT INTO categories (id, name) VALUES
(1, 'wood'),
(2, 'luxury'),
(3, 'vintage'),
(4, 'modern'),
(5, 'super luxury');

SELECT c.name, SUM(p.amount)
FROM categories c 
JOIN products p ON p.id_categories = c.id
GROUP BY c.name
ORDER BY c.name;