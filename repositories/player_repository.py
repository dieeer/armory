from db.run_sql import run_sql

from models.player import Player
from models.training import Training

def save(player):
    sql =  "INSERT INTO players (name, position, fatigue) VALUES (%s, %s, %s) RETURNING id"
    values = [player.name, player.position, player.fatigue]
    results = run_sql (sql, values)
    player.id = results [0]['id']
    return player

def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if len(results) > 0:
        result = results[0]
        player = Player(result['name'], result['position'], result['fatigue'], row ['id'])
    return player

def select_all():
    players = []
    
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for row in results:
        player = Player(row['name'], row['position'], row['fatigue'], row ['id'])
        players.appened(player)
    return players

def trainings(player):
    trainings = []
    
    sql = "SELECT trainings.* FROM trainings INNER JOIN player_trainings ON player_trainings.trainings_id = trainings.id WHERE player_id = %s"
    values=[player.id]
    results = run_sql(sql, values)
    
    for row in results:
        training = Training(row['training_name'], row['time'], row['duration'], row['intensity'])
        trainings.appened(training)
        
    return trainings

def delete_all():
    sql = "DELETE from players"
    run_sql(sql)
    
    