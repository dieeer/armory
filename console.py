import pdb
from controllers.player_training_controller import player_training
from models.player import Player
from models.training import Training
from models.player_training import Player_Training
from models.current_squad import CurrentSquad

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
player3 = Player('Kieran Tierney', 3, 'LWB', 60)
player_repository.save(player3)
player4 = Player('Aaron Ramsdale', 1, 'GK', 0)
player_repository.save(player4)
player5 = Player('Matty Turner', 30, 'GK', 30)
player_repository.save(player5)
player6 = Player('Hector Bellerin', 2, 'RB', 30)
player_repository.save(player6)
player7 = Player('Ben White', 4, 'CB', 0)
player_repository.save(player7)
player8 = Player('Gabriel', 6, 'CB', 0)
player_repository.save(player8)
player9 = Player('Oleksandr Zinchenko', 35, 'CB', 0)
player_repository.save(player9)
player10 = Player('Martin Ødegaard', 10, 'CM', 0)
player_repository.save(player10)
player11 = Player('Granit Xhaka', 34, 'CM', 0)
player_repository.save(player11)
player12 = Player('Gabriel Martinelli', 11, 'LM', 0)
player_repository.save(player12)
player13 = Player('Gabriel Jesus', 9, 'ST', 0)
player_repository.save(player13)
player14 = Player('Eddie Nketiah', 14, 'ST', 0)
player_repository.save(player14)
player15 = Player('Rob Holding', 16, 'CB', 0)
player_repository.save(player15)
player16 = Player('Takehiro Tomiyasu', 18, 'CB', 0)
player_repository.save(player16)
player17 = Player('Cedric', 17, 'RB', 0)
player_repository.save(player17)


training1 = Training('Warm-up', '13:00', 30, 'low')
training_repository.save(training1)
training2 = Training('Catching and throwing', '13:00', 15, 'medium')
training_repository.save(training2)


player_training1 = Player_Training(player1, training1, "nothing to note")
player_training_repository.save(player_training1)
player_training2 = Player_Training(player4, training2, "solid as usual")
player_training_repository.save(player_training2)



