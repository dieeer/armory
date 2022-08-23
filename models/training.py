from models.player import Player

class Training:
    def __init__(self, training_name, time, duration, intensity, id = None):
        self.training_name = training_name
        self.time = time
        self.duration = duration
        self.intensity = intensity
        self.id = id
        
        
    def training_increases_fatigue(self, player):
        player.raise_fatigue(self.intensity)
        