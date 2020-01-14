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
        for y in range(16):
            ff = f[y].split(',')
            for x in range(16):
                self.board.pole[x][y] = []
                for n in ff[x].split():
                    self.board.pole[x][y].append(n)


    def render(self, events):
        self.board.render(events)
