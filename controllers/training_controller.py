from flask import Flask, render_template, request, redirect, Blueprint

from models.training import Training

import repositories.training_repository as training_repository

training_blueprint = Blueprint("training", __name__)

@training_blueprint.route("/training")
def training():
    training = training_repository.select_all()
    return render_template("training/index.html", training = training)
