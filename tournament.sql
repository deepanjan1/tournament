-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE player (
	userid SERIAL PRIMARY KEY NOT NULL,
	name TEXT NOT NULL);

CREATE TABLE record (
	userid INT REFERENCES player(userid) PRIMARY KEY,
	wins INT,
	losses INT);

CREATE TABLE match (
	winner INT REFERENCES player(userid),
	loser INT REFERENCES player(userid));