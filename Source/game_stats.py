import json

class GameStats:
    """Tracks statistics for Alien Invasion."""

    def __init__(self, ai_game, assets):
        self.settings = ai_game.settings
        self.assets = assets
        self.high_score_file = assets.get_high_score_txt_file()
        self.reset_stats()
        self.game_active = False        ## starts game in an inactive state
        self.open_savegame()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.game_active = True
        self.score = 0
        self.level = 1


    def open_savegame(self):
        try:
            with open(self.high_score_file) as score_file:
                score = json.load(score_file)
                self.high_score = int(score)
        except:
            self.high_score = 0


    def save_game(self):
        with open(self.high_score_file, 'w') as score_file:
            json.dump(self.high_score, score_file)