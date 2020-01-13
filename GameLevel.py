import pygame
import GameObject
import Board


class GameLevel(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.board = Board.Board(screen)

    def loadMap(self, args):
        print('loaded level')

    def loadEntity(self, args):
        print('loaded entity')

    def render(self, events):
        self.board.render(events)
