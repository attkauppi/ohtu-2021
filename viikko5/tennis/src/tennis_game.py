from player import Player
class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(
            player_name=player1_name,
        )
        self.player2 = Player(
            player_name = player2_name
        )

    def won_point(self, player_name):
        if player_name == self.player1.player_name:
            self.player1.won_point()
        else:
            self.player2.won_point()

    def get_score(self):
        score = ""
        temp_score = 0

        # Tasatilanne
        if self.player1.get_score() == self.player2.get_score():
            if self.player1.get_score() == 0:
                score = "Love-All"
            elif self.player1.get_score() == 1:
                score = "Fifteen-All"
            elif self.player1.get_score() == 2:
                score = "Thirty-All"
            elif self.player1.get_score() == 3:
                score = "Forty-All"
            else:
                score = "Deuce"
        # Jomman kumman pisteet 4 tai yli
        elif self.player1.get_score() >= 4 or self.player2.get_score() >= 4:
            minus_result = self.player1.get_score() - self. player2.get_score()

            # Jos erotus 1, advantage p1
            if minus_result == 1:
                score = "Advantage player1"
            # Jos erotus -1, advantage p2
            elif minus_result == -1:
                score = "Advantage player2"
            # Jos erotus yli 2, toinen voittaa
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        # Muuten pelitilannetta tutkitaan näin
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1.get_score()
                else:
                    score = score + "-"
                    temp_score = self.player2.get_score()

                # If i == 1, kirjoittaa scoreen m_score 1:sen
                # Muuten kirjoittaa scoreen m_score 2:sen
                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
