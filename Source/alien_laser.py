from pygame.sprite import Sprite


class Alien_Laser(Sprite):
    def __init__(self, ai_game, pos, assets):
        super().__init__()
        self.assets = assets
        self.image = self.assets.get_image("green_laser")
        self.rect = self.image.get_rect(center = pos)
        self.settings = ai_game.settings
        self.screen = ai_game.screen


    def update(self):
        """Moves the laser down the screen."""
        self.rect.y -= self.settings.alspeed
        self.destroy()


    def destroy(self):
        """Destroys the laser once it exits the screen."""
        if self.rect.y >= self.settings.screen_height:
            self.kill()


    def draw_laser(self):
        """Draw the laser to the screen."""
        self.screen.blit(self.image, self.rect)
