from flask import Flask, render_template, request, redirect, Blueprint

from models.training import Training

import repositories.training_repository as training_repository

trainings_blueprint = Blueprint("trainings", __name__)

@trainings_blueprint.route("/trainings")
def trainings():
    trainings = training_repository.select_all()
    return render_template("trainings/index.html", trainings = trainings)
