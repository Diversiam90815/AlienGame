from pygame.sprite import Sprite

class Explosion(Sprite):
    def __init__(self, assets):
        super().__init__()
        self.assets = assets        
        self.images = self.assets.get_explosion_images()
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
