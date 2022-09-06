from db.run_sql import run_sql
from models.current_squad import CurrentSquad

from models.player import Player
from models.training import Training
from models.player_training import Player_Training

import repositories.player_repository as player_repository
import repositories.training_repository as training_repository
import repositories.player_training_repository as player_training_repository

def save(current_squad):
    sql = "INSERT INTO current_squad (gk_id, lb_id, cb1_id, cb2_id, rb_id, lm_id, cm1_id, cm2_id, rm_id, cam_id, st_id, sub1_id, sub2_id, sub3_id, sub4_id, sub5_id, sub6_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [current_squad.gk.id, current_squad.lb.id, current_squad.cb1.id, current_squad.cb2.id, current_squad.rb.id, current_squad.lm.id, current_squad.cm1.id, current_squad.cm2.id, current_squad.rm.id, current_squad.cam.id, current_squad.st.id, current_squad.sub1.id, current_squad.sub2.id, current_squad.sub3.id, current_squad.sub4.id, current_squad.sub5.id, current_squad.sub5.id]
    results = run_sql(sql, values)
    current_squad.id = results [0]['id']
    return results

def select():
    teamsheet = []
    sql = "SELECT * FROM current_squad"
    result = run_sql(sql)[0]
    
    if len(result) > 0:
        current_squad = CurrentSquad(result['gk_id'], result['lb_id'], result['cb1_id'], result['cb2_id'], result['rb_id'], result['lm_id'], result['cm1_id'], result['cm2_id'], result['rm_id'], result['cam_id'], result['st_id'], result['sub1_id'], result['sub2_id'], result['sub3_id'], result['sub4_id'], result['sub5_id'], result['sub6_id'], result['id'])
        teamsheet.append(current_squad)
    return teamsheet

def player(current_squad):
    sql = 'SELECT * FROM players WHERE id = %s'
    values = [current_squad.player.id]
    results = run_sql(sql,values)[0]
    player = Player(results['name'], results['shirt_no'], results['position'], results['fatigue'], results['id'])
    return player

def get_player_with_id(player):
    current_squad = []
    
    sql = "SELECT players.* FROM players INNER JOIN current_squad ON current_squad.*_id = current_squad.*.id  WHERE player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)
    
    for row in results:
        player = Player(row['name'], row['shirt_no'], row['position'], row['fatigue'], row['id'])
        current_squad.append(player)
    print(current_squad)
    return current_squad

def delete_all():
    sql = "DELETE FROM current_squad"
    run_sql(sql)
    
    