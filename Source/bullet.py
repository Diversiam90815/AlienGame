from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game, assets):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.assets = assets
        self.settings = ai_game.settings
        self.image = self.assets.get_image("red_laser")
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)             ## saves the bullets position as a float


    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y


    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
