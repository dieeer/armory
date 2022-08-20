import pdb
from controllers.player_training_controller import player_training
from models.player import Player
from models.training import Training
from models.player_training import Player_Training

import repositories.player_repository as player_repository
import repositories.training_repository as training_repository
import repositories.player_training_repository as player_training_repository

player_repository.delete_all()
training_repository.delete_all()
player_training_repository.delete_all()

player1 = Player('Bukayo Saka', 7, 'RW', 1)
player_repository.save(player1)

player2 = Player('Emile Smith-Rowe', 10, 'CAM', 10)
player_repository.save(player2)

player3 = Player('Kieran Tierney', 2, 'LWB', 60)
player_repository.save(player3)

player4 = Player('Aaron Ramsdale', 1, 'GK', 0)
player_repository.save(player4)


training1 = Training('Warm-up', '13:00', 30, 'low')
training_repository.save(training1)

training2 = Training('Catching and throwing', '13:00', 15, 'medium')
training_repository.save(training2)



player_training1 = Player_Training(player1, training1, "nothing to note")
player_training_repository.save(player_training1)

player_training2 = Player_Training(player4, training2, "solid as usual")
player_training_repository.save(player_training2)


