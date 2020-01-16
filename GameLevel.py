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
        global hodingPoint
        global hod
        self.board.levelN = args
        f = open("data\\levels\\"+str(args)+".level").read().split('\n')
        for y in range(16):
            ff = f[y].split(',')
            for x in range(16):
                self.board.pole[x][y] = []
                for n in ff[x].split():
                    if n[0] == 'e':
                        if n[1] == 'p':
                            self.board.playerEntity.append((x,y))
                        else:
                            self.board.EnemyEntity.append((x,y))
                    self.board.pole[x][y].append(n)
        hodingPoint = self.board.playerEntity[0]
        hod = 0


    def render(self, events):
        self.board.render(events)
