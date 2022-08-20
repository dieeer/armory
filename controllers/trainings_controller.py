from crypt import methods
from flask import Flask, render_template, request, redirect, Blueprint

from models.player import Player
from models.training import Training
from models.player_training import Player_Training

import repositories.player_repository as player_repository
import repositories.training_repository as training_repository
import repositories.player_training_repository as player_training_repository

trainings_blueprint = Blueprint("trainings", __name__)

@trainings_blueprint.route("/trainings")
def trainings():
    trainings = training_repository.select_all()
    return render_template("trainings/index.html", trainings = trainings)

# @trainings_blueprint.route('/trainings/<id>')
# def show(id):
#     player = player_repository.select(id)
#     trainings = player_repository.trainings(player)
#     return render_template('players/show.html', player = player, trainings = trainings)

@trainings_blueprint.route('/trainings/new', methods=['GET'])
def new_trainings():
    players = player_repository.select_all()
    return render_template('/trainings/new.html', players = players)

@trainings_blueprint.route('/trainings', methods=['POST'])
def create_trainings():
    training_name = request.form['training_name']
    time = request.form['time']
    duration = request.form['duration']
    intensity = request.form['intensity']
    new_training = Training(training_name, time, duration, intensity)
    training_repository.save(new_training)
    return redirect('/trainings')