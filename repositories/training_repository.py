from db.run_sql import run_sql

from models.player import Player
from models.training import Training

def save(training):
    sql = "INSERT INTO trainings(training_name, time, duration, intensity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [training.training_name, training.time, training.duration, training.intensity]
    results = run_sql(sql, values)
    training.id = results[0]['id']
    return training

def select_all():
    trainings = []
    sql = "SELECT * FROM trainings"
    results = run_sql(sql)
    
    for row in results:
        training = Training(row['training_name'], row['time'], row['duration'], row['intensity'], row['id'])
        trainings.append(training)
    return trainings

def select(id):
    training = None
    sql = "SELECT * FROM trainings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        training = Training(result['training_name'], result['time'], result['duration'], result ['intensity'], result['id'])
    return training

def players(training):
    players = []
    
    sql = "SELECT players.* FROM players INNER JOIN players_trainings ON players_trainings.player_id = players.id WHERE training_id = %s"
    values = [training.id]
    results = run_sql(sql, values)
    
    for row in results:
        player = Player(row['name'], row['shirt_no'], row['position'], row['fatigue'], row ['id'])
        players.append(player)
    return players

def delete_all():
    sql = "DELETE FROM trainings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM trainings WHERE id = %s"
    values =[id]
    run_sql(sql, values)
        
def update(training):
    sql = "UPDATE trainings SET (training_name, time, duration, intensity) = (%s, %s, %s, %s) WHERE id = %s"
    values = [training.training_name, training.time, training.duration, training.intensity, training.id]
    run_sql(sql, values)
    
    
