-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;

-- connect to the tournament database
\c tournament

-- create schema
CREATE TABLE player (
    id serial primary key,
    name text,
    wins integer,
    total_matches integer);
