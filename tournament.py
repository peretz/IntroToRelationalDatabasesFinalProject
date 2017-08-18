#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    database = connect()
    cursor = database.cursor()
    try:
        cursor.execute("DELETE FROM match")
        database.commit()
    except:
        database.rollback()
    database.close()


def deletePlayers():
    """Remove all the player records from the database."""

    database = connect()
    cursor = database.cursor()
    try:
        cursor.execute("DELETE FROM player")
        database.commit()
    except:
        database.rollback()
    database.close()


def countPlayers():
    """Returns the number of players currently registered."""

    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT count(*) FROM player;")
    total_players = cursor.fetchone()[0]
    database.close()

    return total_players


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    database = connect()
    cursor = database.cursor()
    try:
        cursor.execute("INSERT INTO player(name) VALUES (%s)", (name,))
        database.commit()
    except:
        database.rollback()

    database.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM player_stats")
    standings = cursor.fetchall()
    database.close()

    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    database = connect()
    cursor = database.cursor()
    try:
        cursor.execute("INSERT INTO match(winner, loser) VALUES (%s, %s)",
                       (winner, loser,))
        database.commit()
    except:
        database.rollback()
    database.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT id, name FROM player_stats")
    standings = cursor.fetchall()
    pairings = list()
    for i in range(0, len(standings), 2):
        pairings.append(standings[i] + standings[i+1])

    database.close()

    return pairings
