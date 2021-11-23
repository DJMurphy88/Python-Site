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
    return render_template("Index.html")

@app.route("/collection")
def collection():
    Database.connect()
    games = Database.get_games()
    Database.close()
    return render_template("Collection.html", games=games)

@app.route("/listGames")
def listGames():
    return render_template("List.html")

@app.route("/submission")
def submission():
    return render_template("Submission.html")

@app.route("/submission", methods = ['POST'])
def getFormData():
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
        game = Game(title, filename, system, release_date, genre, completed)
        Database.connect()
        Database.add_game(game)
        Database.close()
    return redirect("collection")

@app.route("/update")
def update():
    return render_template("Update.html")
