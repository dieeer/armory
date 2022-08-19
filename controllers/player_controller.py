from flask import Flask, render_template, request, redirect, Blueprint

from models.player import Player

import repositories.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players = players)
