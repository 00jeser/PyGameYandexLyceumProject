import pygame
import GameObject


class Board(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def render(self, events):
        pass
