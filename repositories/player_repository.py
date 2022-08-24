from db.run_sql import run_sql

from models.player import Player
from models.training import Training
def save(player):
    sql =  "INSERT INTO players (name, shirt_no, position, fatigue) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [player.name, player.shirt_no, player.position, player.fatigue]
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
        player = Player(result['name'], result['shirt_no'], result['position'], result['fatigue'], result['id'])
    return player

def select_all():
    players = []
    
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for row in results:
        player = Player(row['name'], row['shirt_no'], row['position'], row['fatigue'], row ['id'])
        players.append(player)
    return players

def delete_all():
    sql = "DELETE from players"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values =[id]
    run_sql(sql, values)
    
def update(player):
    sql = "UPDATE players SET (name, shirt_no, position, fatigue) = (%s, %s, %s, %s) WHERE id = %s"
    values = [player.name, player.shirt_no, player.position, player.fatigue, player.id]
    run_sql(sql, values)
    
def get_training_for_player_with_id(player):
    trainings = []
    
    sql = "SELECT trainings.* FROM trainings INNER JOIN players_trainings ON players_trainings.training_id = trainings.id  WHERE player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)
    
    for row in results:
        training = Training(row['training_name'], row['time'], row['duration'], row['intensity'], row['id'])
        trainings.append(training)
    print(trainings)
    return trainings

def is_player_first_team(player):
    player.is_player_match_fit(player)
    
def squad(squad_id):
    players = []
    
    sql = "SELECT * FROM  WHERE id = %s"
    values = [squad_id]
    results = run_sql(sql, values)
    print(results)
    
    for row in results:
        player_gk = select(row['gk_id'])
        player_lb = select(row['lb_id'])
        player_cb1 = select(row['cb1_id'])
        player_cb2 = select(row['cb2_id'])
        player_rb = select(row['rb_id'])
        player_lm = select(row['lm_id'])
        player_cm1 = select(row['cm1_id'])
        player_cm2 = select(row['cm2_id'])
        player_rm = select(row['rm_id'])
        player_cam = select(row['cam_id'])
        player_st = select[row['st_id']]
        player_sub1 = select(['sub1_id'])
        player_sub2 = select(['sub2_id'])
        player_sub3 = select(['sub3_id'])
        player_sub4 = select(['sub4_id'])
        player_sub5 = select(['sub5_id'])
        player_sub6 = select(['sub6_id'])
        players.append(player_gk)
        players.append(player_lb)
        players.append(player_cb1)
        players.append(player_cb2)
        players.append(player_rb)
        players.append(player_lm)
        players.append(player_cm1)
        players.append(player_cm2)
        players.append(player_rm)
        players.append(player_cam)
        players.append(player_st)
        players.append(player_sub1)
        players.append(player_sub2)
        players.append(player_sub3)
        players.append(player_sub4)
        players.append(player_sub5)
        players.append(player_sub6)
    print(players)
    return players
        
        