import unittest

from models.player import Player
from console import *

class TestPlayer(unittest.TestCase):
    def test_player_has_name(self):
        self.assertEqual("Bukayo Saka", player1.name)
        
    def test_player_has_shirt(self):
        self.assertEqual(7, player1.shirt_no)
    
    def test_player_has_position(self):
        self.assertEqual('RW', player1.position)
    
    def test_player_has_fatigue(self):
        self.assertEqual(1, player1.fatigue)
        
    def test_can_raise_fatigue(self):
        player1.raise_fatigue(1)
        self.assertEqual(2, player1.fatigue)