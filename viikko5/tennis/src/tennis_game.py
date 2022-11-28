class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name

        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.highest_score() < 4:
            return self.low_scores()
        else:
            return self.high_scores()
    
    def low_scores(self):
        scores = {
            0 : "Love",
            1 : "Fifteen",
            2 : "Thirty",
            3 : "Forty",
        }
        if self.even():
            return f"{scores[self.player1_score]}-All"
        else:
            return f"{scores[self.player1_score]}-{scores[self.player2_score]}"
    
    def high_scores(self):
        if self.even():
            return "Deuce"
        elif self.difference() == 1:
            return f"Advantage {self.advantage()}"
        else:
            return f"Win for {self.advantage()}"

    def highest_score(self):
        return max(self.player1_score, self.player2_score)

    def even(self):
        return self.player1_score == self.player2_score

    def difference(self):
        return abs(self.player1_score-self.player2_score)

    def advantage(self):
        if self.player1_score > self.player2_score:
            return "player1"
        elif self.player2_score > self.player1_score:
            return "player2"
        return None