from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.player import Player
from models.club import Club
from app import db


player_blueprint = Blueprint("players", __name__)

@player_blueprint.route("/players")
def get_players():
    
    club1 = Club(club_name="Hearts")
    club2 = Club(club_name="Hibernian")

    db.session.add(club1)
    db.session.add(club2)

    db.session.commit()

    player1 = Player(name="Craig Gordon", age=40, position="Goalkeeper", club_id = club1.id)
    player2 = Player(name="David Marshall", age=38, position="Goalkeeper", club_id = club2.id)

    db.session.add(player1)
    db.session.add(player2)

    db.session.commit()
    
    clubs_from_db = Club.query.all()
    players_from_db = Player.query.all()

    return render_template("index.jinja", players=players_from_db, clubs=clubs_from_db)

@player_blueprint.route("/players", methods=["POST"])
def save_player():
    player_name = request.form["name"]    
    player_age = request.form["age"]    
    player_position = request.form["position"]    
    player_club_id = request.form["clubs"]
    player_to_save = Player(name=player_name, age=player_age, position=player_position, club_id=player_club_id)
    db.session.add(player_to_save)
    db.session.commit()
    return redirect("/players")  

@player_blueprint.route("/players/<int:id>")  
def view_player(id):
    clubs_from_db = Club.query.all()
    players_from_db = Player.query.all()
    for player in players_from_db:
        print(f'ID WE ARE LOOKING FOR {id}')
        print(player.id)
        if player.id == id:
            return render_template("player_details.jinja", player=player, clubs=clubs_from_db)

@player_blueprint.route("/players/<int:player_id>", methods=['POST'])
def update_player(player_id):
    player_to_update = Player.query.get(player_id)
    player_to_update.name = request.form['name']
    player_to_update.age = request.form['age']
    player_to_update.position = request.form['position']
    player_to_update.club_id = int(request.form['club_id'])
    db.session.commit()
    return redirect(f"/players/{player_id}")



