from db.run_sql import run_sql

from models.player import Player
from models.training import Training
from models.player_training import Player_Training

import repositories.player_repository as player_repository
import repositories.training_repository as training_repository
import repositories.player_training_repository as player_training_repository

def save(player_training):
    sql = "INSERT INTO players_trainings  (player_id, training_id, comments) VALUES (%s, %s, %s) RETURNING id"
    values = [player_training.player.id, player_training.training.id, player_training.comments]
    results = run_sql (sql, values)
    player_training.id = results [0]['id']
    return player_training

def select(id):
    player_training = None
    sql = "SELECT * FROM players_trainings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        player_training = Player_Training(result['player_id'], result['training_id'], result['comments'])
    return player_training

def select_all():
    player_trainings = []
    
    sql = 'SELECT * FROM players_trainings'
    results = run_sql(sql)
    
    for row in results:
        player = player_repository.select(row['player_id'])
        training = training_repository.select(row['training_id'])
        player_training = Player_Training(player, training, row['comments'], row['id'])
        player_trainings.append(player_training)
    return player_trainings

def training(player_training):
    sql = 'SELECT * FROM trainings WHERE id = %s'
    values = [player_training.training.id]
    results = run_sql(sql, values)[0]
    training = Training(results['training_name'], results['time'], results['duration'], results['intensity'], results['id'])

    return training

def player(player_training):
    sql = 'SELECT * FROM players WHERE id = %s'
    values = [player_training.player.id]
    results = run_sql(sql, values)[0]
    player = Player(results['name'], results['shirt_no'], results['position'], results['fatigue'], results['id'])
    return player

def delete_all():
    sql = "DELETE FROM players_trainings"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE FROM players_trainings WHERE id = %s"
    values =[id]
    run_sql(sql, values)