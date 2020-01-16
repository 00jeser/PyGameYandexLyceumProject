import pygame
import GameObject
import MenuLevel
import GameLevel
import EndLevel


class levelManeger(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.currentLevel = 0
        self.levels = [MenuLevel.MenuLevel(
            screen), GameLevel.GameLevel(screen), EndLevel.EndLevel(screen)]

    def init(self, modules):
        super().init(modules)
        for i in self.levels:
            i.init(modules)

    def render(self, events):
        self.levels[0].init(self.modules)
        self.levels[self.currentLevel].render(events)

    def setLevel(self, n, args=0):
        self.levels[1] = GameLevel.GameLevel(self.screen)
        self.levels[1].init(self.modules)
        if n == 1:
            self.levels[1].loadMap(args)
        if n == 2:
            self.levels[2] = EndLevel(self.screen, *args)
        self.currentLevel = n
