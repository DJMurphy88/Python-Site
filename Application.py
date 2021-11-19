import Database
from flask import Flask, render_template

app = Flask(__name__)

app.config['UPLOAD_PATH'] = "/static/images"

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

@app.route("/update")
def update():
    return render_template("Update.html")
