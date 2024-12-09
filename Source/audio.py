import pygame
from random import choice

pygame.init()
#pygame.mixer.init()

class Audio:
    def __init__(self):
        pygame.mixer.pre_init(frequency=48000)
        '''Initialize the sound effects.'''
        self.bullet01 = pygame.mixer.Sound('../Assets/audio/SFX/Bullet 01.wav')
        self.bullet02 = pygame.mixer.Sound('../Assets/audio/SFX/Bullet 02.wav')
        self.bullet03 = pygame.mixer.Sound('../Assets/audio/SFX/Bullet 03.wav')
        self.bullet04 = pygame.mixer.Sound('../Assets/audio/SFX/Bullet 04.wav')
        self.bullet05 = pygame.mixer.Sound('../Assets/audio/SFX/Bullet 05.wav')
        self.btnClick01 = pygame.mixer.Sound('../Assets/audio/SFX/Button Click 01.wav')
        self.btnClick02 = pygame.mixer.Sound('../Assets/audio/SFX/Button Click 02.wav')
        self.btnExit01 = pygame.mixer.Sound('../Assets/audio/SFX/Exit BTN 01.wav')
        self.btnExit02 = pygame.mixer.Sound('../Assets/audio/SFX/Exit BTN 02.wav')
        self.btnExit03 = pygame.mixer.Sound('../Assets/audio/SFX/Exit BTN 03.wav')
        self.explosion01 = pygame.mixer.Sound('../Assets/audio/SFX/Explosion 01.wav')
        self.explosion02 = pygame.mixer.Sound('../Assets/audio/SFX/Explosion 02.wav')
        self.explosion03 = pygame.mixer.Sound('../Assets/audio/SFX/Explosion 03.wav')
        self.laser01 = pygame.mixer.Sound('../Assets/audio/SFX/Laser 01.wav')
        self.ship_hit = pygame.mixer.Sound('../Assets/audio/SFX/Ship got hit.wav')


    def sfx_bullet(self):
        bullet_sounds = [self.bullet01, self.bullet02, self.bullet03, self.bullet04, self.bullet05]
        rand_bul_sfx = choice(bullet_sounds)
        rand_bul_sfx.play()

    def sfx_explosion(self):
        explosion_sounds = [self.explosion01, self.explosion02, self.explosion03]
        rand_exp_sfx = choice(explosion_sounds)
        rand_exp_sfx.play()

    def sfx_btnclick(self):
        button_click_sounds = [self.btnClick01, self.btnClick02]
        rand_btn_sfx = choice(button_click_sounds)
        rand_btn_sfx.play()
        
    def sfx_exit(self):
        exit_sounds = [self.btnExit01, self.btnExit02, self.btnExit03]
        rand_ex_sfx = choice(exit_sounds)
        rand_ex_sfx.play()

    def sfx_laser(self):
        laser_sounds = [self.laser01]
        rand_las_sfx = choice(laser_sounds)
        rand_las_sfx.play()

    def sfx_ship_hit(self):
        ship_hit_sounds = [self.ship_hit]
        rand_ship_hit_sfx = choice(ship_hit_sounds)
        rand_ship_hit_sfx.play()
