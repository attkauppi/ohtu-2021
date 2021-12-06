
from functools import total_ordering
class Player:
    def __init__(self, player_name, points=0):
        self.player_name = player_name
        self.points = points
    
    def add_point(self):
        self.points += 1

    def get_points(self):
        return self.points
    
    def has_four_or_more_points(self):
        if self.points >= 4:
            return True
        return False
    
    def __lt__(self, other):
        """ Less than method
        https://www.pythonpool.com/python-__lt__/
        """
        if self.get_points() > other.get_points():
            return True
        return False
    
    def __eq__(self, other):
        return self.get_points() == other.get_points()

