DROP DATABASE IF EXISTS shopcart;
CREATE DATABASE shopcart;
USE shopcart;

DROP TABLE IF EXISTS product;
CREATE TABLE product(
id_product INT AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
description VARCHAR(500),
brand VARCHAR(50),
price FLOAT NOT NULL,
discount FLOAT,
quantity INT NOT NULL,
url_img VARCHAR(50),
PRIMARY KEY (id_product)
);

DROP TABLE IF EXISTS cart;
CREATE TABLE cart(
id_cart INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY (id_cart)
);

DROP TABLE IF EXISTS cartproduct;
CREATE TABLE cartproduct(
id_cartproduct INT NOT NULL AUTO_INCREMENT,
id_cart INT NOT NULL,
id_product INT NOT NULL,
quantity INT NOT NULL,
PRIMARY KEY (id_cartproduct),
CONSTRAINT fk_product FOREIGN KEY (id_product)
        REFERENCES product (id_product),
CONSTRAINT fk_cart FOREIGN KEY (id_cart)
        REFERENCES cart (id_cart)
);
