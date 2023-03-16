-- resources Table:
CREATE TABLE IF NOT EXISTS resources (
    id int NOT NULL AUTO_INCREMENT,
    item varchar(50) NOT NULL,
    amount int NOT NULL,
    PRIMARY KEY (id)
);

-- sandwiches table:
CREATE TABLE IF NOT EXISTS sandwiches (
id int NOT NULL AUTO_INCREMENT,
sandwich_size varchar(50) NOT NULL,
price float NOT NULL,
PRIMARY KEY (id)
);