-- people определение

-- Drop table

-- DROP TABLE people;

CREATE TABLE people (
	person text NULL,
	region text NULL
);


INSERT INTO people (person,region) VALUES
	 ('Anna Andreadi','West'),
	 ('Chuck Magee','East'),
	 ('Kelly Williams','Central'),
	 ('Cassandra Brandow','South');
