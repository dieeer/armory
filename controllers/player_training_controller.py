from flask import Flask, render_template, request, redirect, Blueprint
from models.player_training import Player_Training
import repositories.player_repository as player_repository
import repositories.training_repository as training_repository

player_training_blueprint = Blueprint("player_training", __name__)

@player_training_blueprint.route("player_training")
def player_training():
    player_training = player_training_repository.select_all()
    return render_template('player_training/index.html', player_training = player_training)