CREATE DATABASE ex1;
USE ex1;

CREATE TABLE customers( id numeric primary key,
 name varchar(255),
 street varchar(255),
 city varchar(255),
 state varchar(2),
 credit_limit numeric
 );
 
CREATE TABLE orders( id int primary key,
 orders_date date,
 id_customers integer references customers(id)
 );
 
INSERT INTO customers (id, name, street, city, state, credit_limit) VALUES
(1, 'Nicollas Diogo Cardoso', 'Acesso Um', 'Porto Alegre', 'RS', 4175),
(2, 'Cecília Olívia Rodrigues', 'Rua Sizuka Usuy', 'Cianorte', 'PR', 3170),
(3, 'Augusto Fernando Carlos Eduardo Cardoso', 'Rua Baldomiro Koerich', 'Palhoça', 'SC', 1967),
(4, 'Nicollas Diogo Cardoso', 'Acesso Um', 'Porto Alegre', 'RS', 4175),
(5, 'Sabrina Helôisa Gabriela Barros', 'Rua Engenheiro Tito Marques Fernandes', 'Porto Alegre', 'RS', 4312),
(6, 'Joaquim Diego Lorenzo Araújo', 'Rua Vittório', 'Novo Hamburgo', 'RS', 2314);

INSERT INTO orders (id, orders_date, id_customers) VALUES
(1, '2016-05-13', 3),
(2, '2016-01-12', 2),
(3, '2016-04-18', 5),
(4, '2016-09-07', 4),
(5, '2016-02-13', 6),
(6, '2016-08-05', 3);

SELECT c.name, o.id
FROM customers c
JOIN orders o ON c.id = o.id_customers
WHERE o.orders_date BETWEEN '2016-01-01' AND '2016-06-30';