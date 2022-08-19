import pdb
from models.player import Player
from models.training import Training

import repositories.player_repository as player_repository
import repositories.training_repository as training_repository

player_repository.delete_all()


player1 = Player('Bukayo Saka', 7, 'RW', 1)
player_repository.save(player1)

player2 = Player('Emile Smith-Rowe', 10, 'CAM', 10)
player_repository.save(player2)

player3 = Player('Kieran Tierney', 2, 'LWB', 60)
player_repository.save(player3)


training1 = Training('Warm-up', '13:00', 30, 'low')
training_repository.save(training1)