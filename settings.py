import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize game's static settings."""
        self.screen_width = 1280
        self.screen_height = 900
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.bg_img = pygame.image.load("image/Space_Background.jpg")
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 8
        self.alien_speed = 1.5
        self.fleet_drop_speed = 15
        self.speedup_scale = 1.3
        self.speedup_scale2 = 1.1
        self.speedup_scale3 = 0.95
        self.score_scale = 1.5
        self.alspeed = -8
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings that change throughout the game."""
        self.ship_speed = 5.0
        self.bullet_speed = 5.0
        self.alien_speed = 2.0
        self.fleet_direction = 1            ## 1 for right, -1 for left
        self.alien_points = 50
        self.alaser_timer = 1000

    def increase_speed(self):
        """Increase the speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale2
        self.alaser_timer *= self.speedup_scale3
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
