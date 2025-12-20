CREATE TABLE Person (
    personId INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50)
);

CREATE TABLE Address (
    addressId INT PRIMARY KEY,
    personId INT,
    city VARCHAR(50),
    state VARCHAR(50)
);

INSERT INTO Person (personId, firstName, lastName) VALUES
(1, 'John', 'Doe'),
(2, 'Jane', 'Smith'),
(3, 'Alice', 'Brown'),
(4, 'Bob', 'Taylor');

INSERT INTO Address (addressId, personId, city, state) VALUES
(1, 1, 'New York', 'NY'),
(2, 2, 'Los Angeles', 'CA'),
(3, 4, 'Chicago', 'IL');


# Write your MySQL query statement below
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address
    ON Person.personId = Address.personId