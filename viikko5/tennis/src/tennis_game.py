class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        temp_score = 0

        # Tasatilanne
        if self.m_score1 == self.m_score2:
            if self.m_score1 == 0:
                score = "Love-All"
            elif self.m_score1 == 1:
                score = "Fifteen-All"
            elif self.m_score1 == 2:
                score = "Thirty-All"
            elif self.m_score1 == 3:
                score = "Forty-All"
            else:
                score = "Deuce"
        # Jomman kumman pisteet 4 tai yli
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2

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
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

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
