class Player:
    def __init__(self, player_name, points=0):
        self.player_name = player_name
        self.points = points
    
    def add_point(self):
        self.points += 1

    def get_points(self):
        return self.points