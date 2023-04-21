class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize game's static settings."""
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        ##self.ship_speed = 1.5
        self.ship_limit = 3
        ##self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        ##self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        ##self.fleet_direction = 1            ## 1 for right, -1 for left
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1            ## 1 for right, -1 for left
        self.alien_points = 50

    def increase_speed(self):
        """Increase the speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
