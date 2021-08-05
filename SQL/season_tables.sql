
DROP TABLE IF EXISTS netflix_spring;

CREATE TABLE netflix_spring (
    show_id VARCHAR(50) PRIMARY KEY,
    show_type VARCHAR(20) NOT NULL,
    title VARCHAR(300),
    director VARCHAR(400),
    show_cast VARCHAR(1000),
    country VARCHAR(300),
    date_added DATE,
    release_year CHAR(4),
    rating VARCHAR(10),
    duration VARCHAR(20),
    listed_in VARCHAR(500)
);

INSERT INTO netflix_spring
  SELECT * FROM netflix
  WHERE MONTH(date_added) BETWEEN 3 AND 5;

DROP TABLE IF EXISTS netflix_summer;

CREATE TABLE netflix_summer (
    show_id VARCHAR(50) PRIMARY KEY,
    show_type VARCHAR(20) NOT NULL,
    title VARCHAR(300),
    director VARCHAR(400),
    show_cast VARCHAR(1000),
    country VARCHAR(300),
    date_added DATE,
    release_year CHAR(4),
    rating VARCHAR(10),
    duration VARCHAR(20),
    listed_in VARCHAR(500)
);

INSERT INTO netflix_summer
  SELECT * FROM netflix
  WHERE MONTH(date_added) BETWEEN 6 AND 8;

DROP TABLE IF EXISTS netflix_fall;

CREATE TABLE netflix_fall (
    show_id VARCHAR(50) PRIMARY KEY,
    show_type VARCHAR(20) NOT NULL,
    title VARCHAR(300),
    director VARCHAR(400),
    show_cast VARCHAR(1000),
    country VARCHAR(300),
    date_added DATE,
    release_year CHAR(4),
    rating VARCHAR(10),
    duration VARCHAR(20),
    listed_in VARCHAR(500)
);

INSERT INTO netflix_fall
  SELECT * FROM netflix
  WHERE MONTH(date_added) BETWEEN 9 AND 11;

DROP TABLE IF EXISTS netflix_winter;

CREATE TABLE netflix_winter (
    show_id VARCHAR(50) PRIMARY KEY,
    show_type VARCHAR(20) NOT NULL,
    title VARCHAR(300),
    director VARCHAR(400),
    show_cast VARCHAR(1000),
    country VARCHAR(300),
    date_added DATE,
    release_year CHAR(4),
    rating VARCHAR(10),
    duration VARCHAR(20),
    listed_in VARCHAR(500)
);

INSERT INTO netflix_winter
  SELECT * FROM netflix
  WHERE MONTH(date_added) = 12
  OR MONTH(date_added) BETWEEN 1 AND 2;