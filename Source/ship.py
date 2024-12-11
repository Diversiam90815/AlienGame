import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game, assets):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.assets = assets
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = self.assets.get_image("ship")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)                         ## saves a float for the center of the ship
        self.moving_right = False                           ## movement flag
        self.moving_left = False

    def update(self):
        """Update the ship's position within screen bounds."""
        if self.moving_right:
            self.x = min(self.x + self.settings.ship_speed, self.screen_rect.right - self.rect.width)
        if self.moving_left:
            self.x = max(self.x - self.settings.ship_speed, 0)
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
