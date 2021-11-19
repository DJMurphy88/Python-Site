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

def make_game(row):
    return Game(row["title"], row["image"], row["system"],
                row["release_date"], row["genre"], row["complete"])

def get_games():
    query = '''SELECT * FROM Games'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    games = []
    for row in results:
        games.append(make_game(row))

    return games

def add_game(game):
    query = '''INSERT INTO Games (title, image, system, release_date, genre, complete) Values(?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, game.getTitle(), game.getImage(), game.getSystem(),
                  game.getDate(), game.getGenre(), game.getComplete())
        conn.commit()

def update_game(title, image, system, date, genre, complete):
    query = '''UPDATE Games SET title = ?, image = ?, system = ?, 
                release_date = ?, genre = ?, complete = ?'''

    with closing(conn.cursor()) as c:
        c.execute(query, (title, image, system, date, genre, complete))
        conn.commit()

def delete_game(title):
    query = '''DELETE FROM Games WHERE title = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (title,))
        conn.commit()
