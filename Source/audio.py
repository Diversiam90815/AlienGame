import pygame
from random import choice

class Audio:
    def __init__(self, assets):
        pygame.mixer.pre_init(frequency=48000)
        '''Initialize the sound effects.'''
        self.bullet01 = assets.get_sound("bullet_01")
        self.bullet02 = assets.get_sound("bullet_02")
        self.bullet03 = assets.get_sound("bullet_03")
        self.bullet04 = assets.get_sound("bullet_04")
        self.bullet05 = assets.get_sound("bullet_05")

        self.btnClick01 = assets.get_sound("button_click_01")
        self.btnClick02 = assets.get_sound("button_click_02")
        
        self.btnExitClick01 = assets.get_sound("button_exit_01")
        self.btnExitClick02 = assets.get_sound("button_exit_02")
        self.btnExitClick03 = assets.get_sound("button_exit_03")

        self.btnExit01 = assets.get_sound("button_exit_01")
        self.btnExit02 = assets.get_sound("button_exit_02")
        self.btnExit03 = assets.get_sound("button_exit_03")

        self.explosion01 = assets.get_sound("explosion_01")
        self.explosion02 = assets.get_sound("explosion_02")
        self.explosion03 = assets.get_sound("explosion_03")

        self.laser01 = assets.get_sound("laser_01")

        self.ship_hit = assets.get_sound("ship_hit")


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
