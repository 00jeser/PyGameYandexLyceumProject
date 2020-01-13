import pygame
import GameObject
import Board


class GameLevel(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.board = Board.Board(screen)
    
    def init(self, modules):
        super().init(modules)
        self.board.init(modules)

    def loadMap(self, args):
        f = open("data\\levels\\"+str(args)+".level").read().split('\n')
        for x in range(16):
            ff = f[x].split(',')
            for y in range(16):
                self.board.pole[x][y] = ff[y].split()


    def render(self, events):
        self.board.render(events)
