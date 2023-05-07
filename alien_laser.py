import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien_Laser(pygame.sprite.Sprite()):
    def __init__(self, pos): 
        super().__init__()
        self.image = pygame.image.load("image/Green_Laser_small")
        self.rect = self.image.get_rect(center = pos)
        self.settings = Settings()

    def update(self):
        self.rect.y -= self.settings.alspeed
        self.destroy()

    def destroy(self):
        if self.rect.y >= self.settings.screen_height:
            self.kill


