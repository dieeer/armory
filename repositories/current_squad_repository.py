from db.run_sql import run_sql

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


    