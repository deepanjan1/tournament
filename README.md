# Tournament 

## Overview
I developed modified the tournament.py file to execute the following functions:
*  Connect to database (`connect()`)
*  Delete all matches (`deleteMatches()`)
*  Delete all players (`deletePlayers()`)
*  Count the number of players (`countPlayers()`)
*  Register a player (`registerPlayer()`)
*  Print out the players standings (`playerStandings()`)
*  Report on match results (`reportMatch()`)
*  Create the swiss pairings for the next match (`swissPairings()`)

## Installation
Download the git contents into one directory.  Then, go through the following steps to create the players database:
```sql
\i tournament.sql
-- Verify that the table was created
\d player
```
Then run the test cases in the command line with the following at the prompt:  `python tournament_test.py`