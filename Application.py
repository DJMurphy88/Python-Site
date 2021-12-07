import os.path

import Database
from Objects import Game
from flask import Flask, render_template, request, abort, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/images'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jfif']

@app.route("/")
def index():
    Database.connect()
    last_game = Database.get_last()
    total_games = Database.get_row_count()
    completed = Database.get_complete()
    system = Database.get_most_system()
    genre = Database.get_most_genre()

    return render_template("index.html", last_game=last_game, total_games=total_games, completed=completed, system=system, genre=genre)

@app.route("/collection", methods=['GET'])
def collection():
    sort = request.args.get('sort')

    Database.connect()
    if sort == "system":
        games = Database.get_games_by_system()

    elif sort == "genre":
        games = Database.get_games_by_genre()

    else:
        games = Database.get_games()
    Database.close()

    return render_template("Collection.html", games=games, sort=sort)

@app.route("/submission")
def submission():
    return render_template("Submission.html")

@app.route("/submission", methods=['POST'])
def getSubmitData():
    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)
    title = request.values["title"]
    system = request.values["system"]
    release_date = request.values["release_date"]
    genre = request.values["genre"]
    completed = request.form.get("completed")
    os.makedirs(app.config['UPLOAD_PATH'], exist_ok=True)

    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        Database.connect()
        gameid = Database.get_row_count() + 1
        game = Game(gameid, title, filename, system, release_date, genre, completed)
        Database.add_game(game)
        Database.close()

    return redirect("collection")

@app.route("/update", methods=['GET'])
def update():
    if request.method == "GET":
        gameid = int(request.args.get('gameid'))
        Database.connect()
        game = Database.get_game(gameid)
        Database.close()

        return render_template("Update.html", game=game)


@app.route("/update", methods=['GET', 'POST'])
def getUpdateData():
    gameid = int(request.args.get('gameid'))
    Database.connect()
    game = Database.get_game(gameid)

    uploaded_file = request.files["file"]
    title = request.values["title"]
    system = request.values["system"]
    release_date = request.values["release_date"]
    genre = request.values["genre"]
    completed = request.form.get("completed")
    os.makedirs(app.config['UPLOAD_PATH'], exist_ok=True)

    if "file" in request.form:
        filename = secure_filename(uploaded_file.filename)
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        os.remove(os.path.join(app.config['UPLOAD_PATH'], game.getImage()))
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

    else:
        filename = game.getImage()

    Database.update_game(gameid, title, filename, system, release_date, genre, completed)
    Database.close()

    return redirect("collection")

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    gameid = int(request.args.get('gameid'))

    Database.connect()
    game = Database.get_game(gameid)
    filename = game.getImage()

    Database.delete_game(gameid)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], filename))
    Database.close()

    return redirect("listGames")
