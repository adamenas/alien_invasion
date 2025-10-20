from pathlib import Path

class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        recorde = Path('recorde.txt')
        self.high_score = recorde.read_text()
    

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.nivel = 1