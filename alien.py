import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a singe alien in the fleet."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('image/Alien2_New_small.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width           ## platziert es an den rechten oberen ecke
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)              ## saves the exact position of the alien
        self.settings = ai_game.settings

    def update(self):
        """Move alien to the right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True