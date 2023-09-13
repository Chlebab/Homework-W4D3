from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/players_app"
db = SQLAlchemy(app)

from models.club import Club
from models.player import Player

migrate = Migrate(app, db)

from controllers.player_contoller import player_blueprint

app.register_blueprint(player_blueprint)


@app.route("/")
def home():
    return "This is the home page!"

