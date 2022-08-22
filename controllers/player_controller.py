from crypt import methods
from flask import Flask, render_template, request, redirect, Blueprint

from models.player import Player
from models.training import Training
from models.player_training import Player_Training

import repositories.player_repository as player_repository
import repositories.training_repository as training_repository
import repositories.player_training_repository as player_training_repository

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players = players)

@players_blueprint.route('/players/<id>')
def show(id):
    player = player_repository.select(id)
    trainings = player_repository.get_training_for_player_with_id(player)
    return render_template('players/show.html', player = player, trainings = trainings)

@players_blueprint.route('/players/new', methods =['GET'])
def new_player():
    players = player_repository.select_all()
    return render_template('/players/new.html', players = players)

@players_blueprint.route('/players', methods =['POST'])
def create_player():
    name = request.form['name']
    shirt_no = request.form['shirt_no']
    position = request.form['position']
    fatigue = request.form['fatigue']
    player = Player(name, shirt_no, position, fatigue)
    player_repository.save(player)
    return redirect('/players')

@players_blueprint.route('/players/<id>/edit', methods=['GET'])
def edit_player(id):
    player = player_repository.select(id)
    return render_template('/players/edit.html', player = player)

@players_blueprint.route('/players/<id>', methods=['POST'])
def update_player(id):
    name = request.form['name']
    shirt_no = request.form['shirt_no']
    position = request.form['position']
    fatigue = request.form['fatigue']
    player = Player(name, shirt_no, position, fatigue, id)
    player_repository.update(player)
    return redirect('/players')

@players_blueprint.route('/players/<id>/delete', methods =['POST'])
def delete_player(id):
    player_repository.delete(id)
    return redirect('/players')
