import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    def __init__(self):
        super().__init__()        
        self.images = []
        for num in range(1,6):
            img = pygame.image.load(f'../Assets/image/Explosions/exp{num}.png')
            img = pygame.transform.scale(img, (160,160))
            self.images.append(img)
        self.index = 0 
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.counter = 0

    def update(self):
        '''updates the animation'''
        EXPLOSION_SPEED = 3
        self.counter += 1
            
        if self.counter >= EXPLOSION_SPEED and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        
        if self.index >= len(self.images) - 1 and self.counter >= EXPLOSION_SPEED: 
            self.images.clear()
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
