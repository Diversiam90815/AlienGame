import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        ## loads the image of the ship.
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        ## place the ship in the middle at the bottom
        self.rect.midbottom = self.screen_rect.midbottom

        ## saves a float for the center of the ship
        self.x = float(self.rect.x)

        ## movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x            ## updates the rect-object based on self.x

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)
