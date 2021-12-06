class Player:
    def __init__(self, player_name, score):
        self.player_name = player_name
        self.score = score
    
    def won_point(self):
        self.score += 1

    def get_score(self):
        return self.score