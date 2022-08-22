from flask import Flask, render_template, request, redirect, Blueprint
from models.player_training import Player_Training
import repositories.player_repository as player_repository
import repositories.training_repository as training_repository
import repositories.player_training_repository as player_training_repository

player_training_blueprint = Blueprint("player_trainings", __name__)

@player_training_blueprint.route("/player_trainings")
def player_training():
    player_training = player_training_repository.select_all()
    return render_template('player_trainings/index.html', player_training = player_training)



@player_training_blueprint.route('/player_trainings/new', methods =['GET'])
def new_player_training():
    players = player_repository.select_all()
    trainings = training_repository.select_all()
    return render_template('/player_trainings/new.html', players = players, trainings = trainings)

@player_training_blueprint.route('/player_trainings', methods =['POST'])
def create_player_training():
    player_id = request.form['player_id']
    training_id = request.form['training_id']
    comments = request.form['comments']
    player = player_repository.select(player_id)
    training = training_repository.select(training_id)
    player_training = Player_Training(player, training, comments)
    player_training_repository.save(player_training)
    return redirect('/player_trainings')

@player_training_blueprint.route('/player_trainings/<id>/delete', methods = ['POST'])
def delete_player_training(id):
    player_training_repository.delete(id)
    return redirect('/player_trainings')