from functools import total_ordering
class Player:
    def __init__(self, name, team, goals=0, assists=0):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    
    def __str__(self):
        return f"{self.name:25} {self.team:10} {self.goals:5} + {self.assists:5} = {self.calculate_points():5}"
 
    def __lt__(self, other):
        """ Less than method
        https://www.pythonpool.com/python-__lt__/
        """
        if self.calculate_points() > other.calculate_points():
            return True
        elif self.calculate_points() == other.calculate_points():
            if self.goals > other.goals:
                return True
            return False
        return False

    def calculate_points(self):
        """ Calculates sum of goals and assists """
        return (self.goals + self.assists)
