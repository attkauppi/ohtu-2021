from operator import attrgetter

# Tämä nyt oli kaikkea paitsi hyvä ratkaisu :'D
class Score:
    def __init__(self, player1, player2):    
        self.players = [player1, player2]

        self.non_endgame_scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

        self.endgame_scores = {
            0: "Deuce",
            1: "Advantage ",
            2: "Win for ",
        }

    def get_point_difference(self):
        return self.players[0].get_points() - self.players[1].get_points()
    
    def get_endgame_score_string(self, point_difference):
        if point_difference >= 2:
            return self.endgame_scores[2]
        else:
            return self.endgame_scores[point_difference]

    def get_endgame_score(self, point_difference, player_with_higher_score=None):
        # Deuce
        if point_difference == 0:
            return self.endgame_scores[point_difference]
        # Not deuce
        return self.get_endgame_score_string(point_difference) + player_with_higher_score.player_name
    
    def get_non_endgame_score(self, point_difference):
        scores = list(map(lambda p: self.non_endgame_scores[p.get_points()], self.players))
        # If points equal, give the first score
        # and add -All at the end.
        if point_difference == 0:
            return scores[0] + "-All"
        return "-".join(scores)
    
    def is_endgame_score(self):
        if any(map(lambda p: p.get_points() >= 4, self.players)):
            return True
        return False
    
    def get_player_with_higher_score(self):
        return max(self.players, key=attrgetter('points'))

    def get_score(self):
        point_difference = abs(self.get_point_difference())

        if self.is_endgame_score():
            return self.get_endgame_score(point_difference, self.get_player_with_higher_score())
        return self.get_non_endgame_score(point_difference)
        

        
        