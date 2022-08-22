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

@trainings_blueprint.route('/trainings/<id>')
def show(id):
    training = training_repository.select(id)
    print(training)
    player = training_repository.players(training)
    print(player)
    return render_template('/trainings/show.html', training = training, player = player)

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

@trainings_blueprint.route('/trainings/<id>/edit', methods=['GET'])
def edit_trainings(id):
    training = training_repository.select(id)
    return render_template('/trainings/edit.html', training = training)

@trainings_blueprint.route('/trainings/<id>', methods = ['POST'])
def update_trainings(id):
    training_name = request.form['training_name']
    time = request.form['time']
    duration = request.form['duration']
    intensity = request.form['intensity']
    training = Training(training_name, time, duration, intensity, id)
    training_repository.update(training)
    return redirect('/trainings')

@trainings_blueprint.route('/trainings/<id>/delete', methods=['POST'])
def delete_training(id):
    training_repository.delete(id)
    return redirect('/trainings')