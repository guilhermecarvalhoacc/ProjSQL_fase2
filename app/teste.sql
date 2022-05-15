DROP DATABASE IF EXISTS shopcart;
CREATE DATABASE shopcart;
USE shopcart;

DROP TABLE IF EXISTS Product;
CREATE TABLE Product(
id_product INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
description VARCHAR(500),
brand VARCHAR(50),
price FLOAT NOT NULL,
discount FLOAT,
quantity INT,
url_img VARCHAR(50)
);
