import pygame
import GameObject


class levelManeger(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.currentLevel = 0
        self.levels = []
    
    def render(self, events):
        self.levels[self.currentLevel].render()
    
    def setLevel(self, n):
        self.currentLevel = n