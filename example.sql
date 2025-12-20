CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  age INT
);

INSERT INTO users (name, age)
VALUES
('Alice', 21),
('Bob', 24);

SELECT * FROM users;
