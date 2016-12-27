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
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM match")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("TRUNCATE player CASCADE")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count(*) AS number FROM player")
    players = c.fetchone()
    DB.close()
    return int(players[0])


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    data = (name, )
    c.execute("INSERT INTO player (name) VALUES (%s)", data)
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
            id: the player's unique id (assigned by the database)
            name: the player's full name (as registered)
            wins: the number of matches the player has won
            matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute(
        "SELECT userid,name,wins,COALESCE(wins+losses,0) FROM standings ORDER BY wins DESC")
    player_wins = c.fetchall()
    DB.commit()
    DB.close()
    return player_wins


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    win = (winner, )
    loss = (loser, )
    c.execute("INSERT INTO match (winner, loser) VALUES (%s,%s)", (win, loss))
    DB.commit()
    DB.close()


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
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT userid,name FROM standings ORDER BY wins DESC")
    player_wins = c.fetchall()
    # c.execute("SELECT count(*) AS num FROM standings")
    num = len(player_wins)
    matches = []
    i = 0
    while i < num:
        matches.append(
            (player_wins[i][0],
             player_wins[i][1],
             player_wins[
                i + 1][0],
                player_wins[
                i + 1][1]))
        i += 2
    DB.commit()
    DB.close()
    return matches
