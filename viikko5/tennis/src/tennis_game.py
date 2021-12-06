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

        # # Tasatilanne
        # if self.player1.get_points() == self.player2.get_points():
        #     if self.player1.get_points() == 0:
        #         score = "Love-All"
        #     elif self.player1.get_points() == 1:
        #         score = "Fifteen-All"
        #     elif self.player1.get_points() == 2:
        #         score = "Thirty-All"
        #     elif self.player1.get_points() == 3:
        #         score = "Forty-All"
        #     # Jos pisteet 4-4, deuce
        #     else:
        #         score = "Deuce"
        # # Jomman kumman pisteet 4 tai yli
        # elif self.player1.get_points() >= 4 or self.player2.get_points() >= 4:
        #     minus_result = self.player1.get_points() - self. player2.get_points()

        #     # Jos erotus 1, advantage p1
        #     if minus_result == 1:
        #         score = "Advantage player1"
        #     # Jos erotus -1, advantage p2
        #     elif minus_result == -1:
        #         score = "Advantage player2"
        #     # Jos erotus yli 2, toinen voittaa
        #     elif minus_result >= 2:
        #         score = "Win for player1"
        #     else:
        #         score = "Win for player2"
        # # Muuten pelitilannetta tutkitaan näin
        # else:
        #     for i in range(1, 3):
        #         if i == 1:
        #             temp_score = self.player1.get_points()
        #         else:
        #             score = score + "-"
        #             temp_score = self.player2.get_points()

        #         # If i == 1, kirjoittaa scoreen m_score 1:sen
        #         # Muuten kirjoittaa scoreen m_score 2:sen
        #         if temp_score == 0:
        #             score = score + "Love"
        #         elif temp_score == 1:
        #             score = score + "Fifteen"
        #         elif temp_score == 2:
        #             score = score + "Thirty"
        #         elif temp_score == 3:
        #             score = score + "Forty"

        # return score
