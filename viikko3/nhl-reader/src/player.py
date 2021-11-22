class Player:
    def __init__(self, name, team, goals=0, assists=0):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    
    def __str__(self):
        return "{} team {} goals {} assists {}".format(
            self.name,
            self.team,
            self.goals,
            self.assists
        )
    
    def __lt__(self, other):
        


    def calculate_points(self):
        """ Calculates sum of goals and assists """
        return self.goals + self.assists

    #@staticmethod
    def compare(item1, item2):
        """ Sorts list of Player objects """
        #https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
        # https://www.pythonpool.com/python-__lt__/
        if item1.calculate_points() < item2.calculate_points():
            return -1
        elif item1.calculate_points() > item2.calculate_points():
            return 1
        else:
            if item1.goals < item2.goals:
                return -1
            elif item1.goals > item2.goals:
                return 1
            else:
                return 0

