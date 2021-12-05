import sqlite3
from contextlib import closing

from Objects import Game

DBFILE = "static/game_db.db"
conn = None

def connect():
    global conn
    conn = sqlite3.connect(DBFILE)
    conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def get_row_count():
    query = '''SELECT COUNT(*) FROM Games'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchone()

    return results[0]

def make_game(row):
    return Game(row["gameid"], row["title"], row["image"], row["system"],
                row["release_date"], row["genre"], row["complete"])

def get_games():
    query = '''SELECT * FROM Games ORDER BY title'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    games = []
    for row in results:
        games.append(make_game(row))

    return games

def get_games_by_system():
    query = '''SELECT * FROM Games ORDER BY system'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    games = []
    for row in results:
        games.append(make_game(row))

    return games

def get_games_by_genre():
    query = '''SELECT * FROM Games ORDER BY genre'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    games = []
    for row in results:
        games.append(make_game(row))

    return games

def get_game(gameid):
    query = '''SELECT * FROM Games WHERE gameid = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, str(gameid))
        result = c.fetchall()

    game = []
    for row in result:
        game.append(make_game(row))

    return game[0]

def add_game(game):
    query = '''INSERT INTO Games (title, image, system, release_date, genre, complete) Values(?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (game.getTitle(), game.getImage(), game.getSystem(),
                  game.getDate(), game.getGenre(), game.getComplete()))
        conn.commit()

def update_game(gameid, title, image, system, date, genre, complete):
    query = '''UPDATE Games
                SET title = ?, image = ?, system = ?, 
                release_date = ?, genre = ?, complete = ?
                WHERE gameid = ?'''

    with closing(conn.cursor()) as c:
        c.execute(query, (title, image, system, date, genre, complete, gameid))
        conn.commit()

def delete_game(gameid):
    query = '''DELETE FROM Games WHERE gameid = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (gameid,))
        conn.commit()

