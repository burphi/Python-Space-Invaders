class GameStats():
    """Track statistics for AI"""

    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start AI in an active state
        self.game_active = False

        # High score should never be reset
        self.read_high_score()

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        """Read the high score from a file"""
        try:
            self.high_score_file = open("high_score.txt", "r")
            self.high_score = int(self.high_score_file.read())
            self.high_score_file.close()
        except FileNotFoundError:
            self.high_score = 0

        return self.high_score

    def write_high_score(self):
        """Write the high score at the end of the game if it is bigger than the previous high score"""
        self.high_score_file = open("high_score.txt", "w")
        self.high_score_file.write(str(self.high_score))
