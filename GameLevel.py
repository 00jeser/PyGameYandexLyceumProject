import GameObject
import pygame
import Board


class GameLevel(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.board = Board(screen)

    def loadMap(self):
        pass

    def loadEntity(self):
        pass

    def render(self, events):
        pass
