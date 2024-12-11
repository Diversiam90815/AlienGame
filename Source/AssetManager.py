import pygame
import os

class AssetManager:
    def __init__(self):
        self.working_directory = os.path.dirname(os.path.abspath(__file__))
        self.images_folder = os.path.join(self.working_directory, "..", "Assets", "Images")
        self.sfx_folder = os.path.join(self.working_directory, "..", "Assets", "Audio")
        self.high_score_file = os.path.join(self.working_directory, "..", "high_score.txt")
        self.images = {}
        self.sounds = {}


    def load_all_assets(self):
        image_map = {
            "green_laser": "Laser/Green_Laser_small.png",
            "red_laser": "Laser/Red_Laser_small.png",
            "alien": "Ship/Alien2_New_small.png",
            "ship": "Ship/Ship_New_small.png",
            "menu_bg": "Background/Space_Background_Menu.jpg",
            "space_bg": "Background/Space_Background.jpg",
            "play_button": "Buttons/Play_Rect.png",
            "options_button": "Buttons/Options_Rect.png",
            "quit_button": "Buttons/Quit_Rect.png",
            "explosion_frame_1": "Explosions/exp1.png",
            "explosion_frame_2": "Explosions/exp2.png",
            "explosion_frame_3": "Explosions/exp3.png",
            "explosion_frame_4": "Explosions/exp4.png",
            "explosion_frame_5": "Explosions/exp5.png",
        }
        self.load_images(image_map)

        sound_map = {
            "bullet_01": "SFX/Bullet/Bullet_01.wav",
            "bullet_02": "SFX/Bullet/Bullet_02.wav",
            "bullet_03": "SFX/Bullet/Bullet_03.wav",
            "bullet_04": "SFX/Bullet/Bullet_04.wav",
            "bullet_05": "SFX/Bullet/Bullet_05.wav",
            "explosion_01": "SFX/Explosion/Explosion_01.wav",
            "explosion_02": "SFX/Explosion/Explosion_02.wav",
            "explosion_03": "SFX/Explosion/Explosion_03.wav",
            "laser_01": "SFX/Laser/Laser_01.wav",
            "button_click_01": "SFX/Button/Button_Click_01.wav",
            "button_click_02": "SFX/Button/Button_Click_02.wav",
            "button_exit_01": "SFX/Button/Exit_BTN_01.wav",
            "button_exit_02": "SFX/Button/Exit_BTN_02.wav",
            "button_exit_03": "SFX/Button/Exit_BTN_03.wav",
            "ship_hit": "SFX/Collision/Ship_Got_Hit.wav",
        }
        self.load_sounds(sound_map)


    def load_images(self, image_map):
        for name, relative_path in image_map.items():
            self.load_image(name, relative_path)


    def load_image(self, name, relative_path):
        full_path = os.path.join(self.images_folder, relative_path)
        image = pygame.image.load(full_path)
        self.images[name] = image


    def get_image(self, name):
        return self.images.get(name)


    def load_sounds(self, sound_map):
        for name, relative_path in sound_map.items():
            self.load_sound(name, relative_path)


    def load_sound(self, name, relative_path):
        full_path = os.path.join(self.sfx_folder, relative_path)
        sound = pygame.mixer.Sound(full_path)
        self.sounds[name] = sound


    def get_sound(self, name):
        return self.sounds.get(name)


    def get_explosion_images(self):
        self.explosion_images = []
        for num in range(1,6):
            img = pygame.image.load(f'{self.images_folder}/Explosions/exp{num}.png')
            img = pygame.transform.scale(img, (160,160))
            self.explosion_images.append(img)
        return self.explosion_images
    

    def get_high_score_txt_file(self):
        return self.high_score_file