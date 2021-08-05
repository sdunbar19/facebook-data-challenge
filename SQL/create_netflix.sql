-- CREATION INSTRUCTIONS

-- wsl
-- sudo service mysql restart
-- sudo mysql -u root -p
-- CREATE DATABASE x
-- USE x
-- source create_table.sql

-- Load CSV - https://caltech.instructure.com/courses/2629/files/303864?module_item_id=86152

DROP TABLE IF EXISTS netflix;

CREATE TABLE netflix(
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

LOAD DATA INFILE '/var/lib/mysql-files/netflix_titles.csv' 
INTO TABLE netflix
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

DROP TABLE IF EXISTS netflix_tv;

CREATE TABLE netflix_tv (
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

INSERT INTO netflix_tv
  SELECT * FROM netflix
  WHERE show_type = 'TV Show';

DROP TABLE IF EXISTS netflix_movie;

CREATE TABLE netflix_movie (
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

INSERT INTO netflix_movie
  SELECT * FROM netflix
  WHERE show_type = 'Movie';