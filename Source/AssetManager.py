import pygame
import os

class AssetManager:
    def __init__(self):
        self.working_directory = os.path.dirname(os.path.abspath(__file__))
        self.images_folder = os.path.join(self.working_directory, "..", "Assets", "Images")
        self.sfx_folder = os.path.join(self.working_directory, "..", "Assets", "Audio")
        self.images = {}
        self.sounds = {}
        self.fonts = {}

    def load_images(self, image_map):
        for name, relative_path in image_map.items():
            self.load_image(name, relative_path)

    def load_image(self, name, relative_path, convert_alpha=True):
        full_path = self.base_path / relative_path
        image = pygame.image.load(str(full_path))
        if convert_alpha:
            image = image.convert_alpha()
        self.images[name] = image

    def get_image(self, name):
        return self.images.get(name)

    def load_sounds(self, sound_map):
        for name, relative_path in sound_map.items():
            self.load_sound(name, relative_path)

    def load_sound(self, name, relative_path):
        full_path = self.base_path / relative_path
        sound = pygame.mixer.Sound(str(full_path))
        self.sounds[name] = sound

    def get_sound(self, name):
        return self.sounds.get(name)

