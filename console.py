import pdb
from models.player import Player
from models.training import Training

import repositories.player_repository as player_repository

player_repository.delete_all()


player1 = Player('Bukayo Saka', 'RW', 0)
player_repository.save(player1)