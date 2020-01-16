import pygame
import random
import GameObject
from os import path


class SoundPlay(GameObject.GameObject):
    def __init__(self, a):
        pygame.mixer.init()
        snd_dir = path.join(path.dirname(__file__), 'data')
        snd_dir = path.join(snd_dir, 'sound')
        pygame.mixer.music.load(path.join(snd_dir, 'music.wav'))
        pygame.mixer.music.play()
        self.hit_sound = pygame.mixer.Sound(path.join(snd_dir, 'hit.wav'))
        self.death_sound = pygame.mixer.Sound(path.join(snd_dir, 'death.wav'))

    def hit(self):
        self.hit_sound.play()

    def death(self):
        self.death_sound.play()
