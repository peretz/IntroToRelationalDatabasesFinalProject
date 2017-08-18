-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

-- Connect to the tournament database.
\c tournament

-- Create schema.
CREATE TABLE player (
    id SERIAL PRIMARY KEY,
    name TEXT);

CREATE TABLE match (
    match_id SERIAL PRIMARY KEY,
    winner INTEGER REFERENCES player(id),
    loser INTEGER REFERENCES player(id));

-- Added views to obtain wins and total matches out of the schema.
CREATE VIEW player_wins AS
    SELECT player.id, player.name, count(match.winner) as wins
    FROM player LEFT JOIN match
    ON player.id = match.winner
    GROUP BY player.id
    ORDER BY wins DESC;

CREATE VIEW player_total_matches AS
    SELECT player.id, player.name, count(match.winner) as total_matches
    FROM player LEFT JOIN match
    ON player.id = match.winner OR player.id = match.loser
    GROUP BY player.id
    ORDER BY total_matches DESC;

CREATE VIEW player_stats AS
    SELECT player.id, player.name, player_wins.wins, player_total_matches.total_matches
    FROM player, player_wins, player_total_matches
    WHERE player.id = player_wins.id AND player.id = player_total_matches.id
    ORDER BY wins DESC, total_matches;

