import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize game's static settings."""
        self.init_static_settings()
        self.init_dynamic_settings()


    def init_dynamic_settings(self):
        """Initialize the settings that change throughout the game."""
        self.ship_speed = 5.0
        self.bullet_speed = 5.0
        self.alien_speed = 2.0
        self.fleet_direction = 1            ## 1 for right, -1 for left
        self.alien_points = 50
        self.alaser_timer = 1000


    def init_static_settings(self):
        """Initialize the settings that are constant throughout the game."""
        self.screen_width = 1280
        self.screen_height = 900
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.font = "Arial"
        self.font_color = "Black"
        self.hover_color = "Red"
        self.menutitle_color = "#b68f40"
        self.btn_font_size = 75
        self.score_color = "White"
        self.dt = self.clock.tick(self.fps) / 1000.0
        self.ship_limit = 3
        self.bullets_allowed = 6
        self.alien_speed = 1.5
        self.fleet_drop_speed = 15
        self.speedup_scale = 1.3
        self.speedup_scale2 = 1.1
        self.speedup_scale3 = 0.95
        self.score_scale = 1.5
        self.alspeed = -8


    def increase_speed(self):
        """Increase the speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale2
        self.alaser_timer *= self.speedup_scale3
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
