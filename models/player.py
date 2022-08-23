class Player:
    def __init__(self, name, shirt_no, position, fatigue, id = None):
        self.name = name
        self.shirt_no = shirt_no
        self.position = position
        self.fatigue = fatigue
        self.id = id
        
    def raise_fatigue(self, addition):
        self.fatigue += addition
        return self.fatigue
    
    def is_player_match_fit(self):
        if self.fatigue >= 60:
            return False
        else:
            return True