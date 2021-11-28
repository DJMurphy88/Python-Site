import sqlite3
from contextlib import closing

from Objects import Game, User

DBFILE = "static/game_db.db"
conn = None

def connect():
    global conn
    conn = sqlite3.connect(DBFILE)
    conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def get_row_count(table):
    query = '''SELECT COUNT(*) FROM ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, table)
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

def get_game(gameid):
    games = get_games()
    for game in games:
        if game.getGameID() == gameid:
            return game

def add_game(game):
    query = '''INSERT INTO Games (title, image, system, release_date, genre, complete) Values(?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (game.getTitle(), game.getImage(), game.getSystem(),
                  game.getDate(), game.getGenre(), game.getComplete()))
        conn.commit()

def update_game(gameid, title, image, system, date, genre, complete):
    query = '''UPDATE Games SET title = ?, image = ?, system = ?, 
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

def make_user(row):
    return User(row["userid"], row["username"], row["password"])

def get_users():
    query = '''SELECT * FROM Users'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    users = []
    for row in results:
        users.append(make_user(row))

    return users

def add_user(user):
    query = '''INSERT INTO Users (username, password) VALUES(?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (user.getUsername(), user.getPassword()))
    conn.commit()
