import pygame
from pygame.sprite import Sprite


#class Explosion(Sprite):
#    def __init__(self):
#        super().__init__()        
#        self.images = []
#        for num in range(1,6):
#            img = pygame.image.load(f'image/Explosions/exp{num}.png')
#            img1 = pygame.transform.scale(img, (160,160))
#            self.images.append(img1)
#        self.index = 0 
#        self.image = self.images[self.index]
#        self.rect = self.image.get_rect()
#        #self.rect.center = (x, y)
#        self.animation_time = 0.1
#        self.current_time = 0


#    def update(self, dt):
#        '''updates the animation'''
#        self.current_time += dt
#        if self.current_time >= self.animation_time:
#            self.current_time = 0
#            self.index += 1
#        #explosion_speed = 3 
#        if self.index >= len(self.images) - 1:
#            self.kill()
#        else:
#            self.image = self.images[self.index]
            

class Explosion(Sprite):
    def __init__(self):
        super().__init__()        
        self.images = []
        for num in range(1,6):
            img = pygame.image.load(f'image/Explosions/exp{num}.png')
            img = pygame.transform.scale(img, (160,160))
            self.images.append(img)
        self.index = 0 
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.counter = 0

    def update(self):
        '''updates the animation'''
        explosion_speed = 3
        self.counter += 1
            
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed: 
            self.images.clear()
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
