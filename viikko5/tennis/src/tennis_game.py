from player import Player
from score import Score
class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(
            player_name=player1_name,
        )
        self.player2 = Player(
            player_name = player2_name
        )
        self.score = Score(self.player1, self.player2)

    def won_point(self, player_name):

        if player_name == self.player1.player_name:
            self.player1.add_point()
        else:
            self.player2.add_point()
        
    def get_score(self):
        return (self.player1.get_points, self.player2.get_points)
    
    def is_endgame_score(self):
        """ Returns True if endgame score """
        return any(map(lambda point: point >= 4, self.get_score()))
    
    def generate_endgame_score(self, score):
        if self.player1.has_four_or_more_points and self.player2.has_four_or_more_points():
            return "Deuce"

    def get_score(self):
        score = ""
        temp_score = 0

        return self.score.get_score()
