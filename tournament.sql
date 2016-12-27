-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- CREATE TABLE player (
-- 	userid SERIAL PRIMARY KEY NOT NULL,
-- 	name TEXT NOT NULL,	
-- 	wins INT DEFAULT 0,
-- 	losses INT DEFAULT 0);


-- Create db and establish schema

DROP DATABASE tournament;
CREATE DATABASE tournament;
\c tournament;


CREATE TABLE player (
	userid SERIAL PRIMARY KEY,
	name TEXT NOT NULL);


--ARCHIVED TABLES
--
-- CREATE TABLE record (
-- 	userid INT REFERENCES player(userid) PRIMARY KEY,
-- 	wins INT DEFAULT 0,
-- 	losses INT DEFAULT 0);

CREATE TABLE match (
	matchid SERIAL PRIMARY KEY,
	winner INT,
	loser INT,
	FOREIGN KEY (winner) REFERENCES player(userid),
	FOREIGN KEY (loser) REFERENCES player(userid));

CREATE VIEW wins AS
	SELECT winner AS userid, count(winner) as wins 
	FROM match 
	GROUP BY userid;

CREATE VIEW losses AS
	SELECT loser AS userid, count(loser) as losses 
	FROM match 
	GROUP BY userid;

CREATE VIEW standings AS
	SELECT player.userid, player.name, COALESCE(wins.wins,0) as wins, COALESCE(losses.losses,0) as losses 
	FROM 
		player 
		LEFT JOIN wins ON player.userid=wins.userid
		LEFT JOIN losses ON player.userid=losses.userid
	ORDER BY wins.wins;

INSERT INTO player(name) VALUES('Deep');
INSERT INTO player(name) VALUES('Harini');
INSERT INTO player(name) VALUES('Minty');
INSERT INTO player(name) VALUES('Azeem');

INSERT INTO match(winner,loser) VALUES(4, 1);
INSERT INTO match(winner,loser) VALUES(3, 2);
INSERT INTO match(winner,loser) VALUES(2, 1);
INSERT INTO match(winner,loser) VALUES(4, 3);