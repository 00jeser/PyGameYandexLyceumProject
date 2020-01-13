import pygame
import GameObject
import MenuLevel
import GameLevel


class levelManeger(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.currentLevel = 0
        self.levels = [MenuLevel.MenuLevel(screen), GameLevel.GameLevel(screen)]
    
    def render(self, events):
        self.levels[0].init(self.modules)
        self.levels[self.currentLevel].render(events)
    
    def setLevel(self, n):
        if n == 1:
            self.levels[1].loadMap()
        self.currentLevel = n