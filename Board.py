import pygame
import GameObject
import math

size = (800, 800)
pos = (100, 100)

hod = 0  # 0-player 1-hoding 2-enemy
hoding = 0
hodingPoint = (0, 0)
errorFlag = False
errorPoint = (-100, -100)


class Board(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.pole = []
        for i in range(16):
            self.pole.append([])
            for _ in range(16):
                self.pole[i].append('')
    
    def GetCoord(self, a):
        return a * (size[0]//16) + pos[0]

    def GetCoords(self, a):
        return (self.GetCoord(a[0]), self.GetCoord(a[1]))

    def render(self, events):
        global hod  # 0-player 1-hoding 2-enemy
        global hoding
        global hodingPoint
        global errorFlag
        global errorPoint
        for i in range(16):
            for ii in range(16):
                p = (size[0]//16*i+pos[0], size[1]//16*ii+pos[1])
                s = (size[0]//16, size[1]//16)
                if hod == 0:
                    if errorFlag:
                        pygame.draw.rect(self.screen, (200, 0, 0),
                                        (*errorPoint, 50, 50), 2)
                    else:
                        pygame.draw.rect(self.screen, (0, 200, 0),
                                        (*errorPoint, 50, 50), 2)
                    pygame.draw.rect(self.screen, (0, 0, 200),
                                     (*self.GetCoords(hodingPoint), 50, 50), 3)
                    for e in self.pole[i][ii]:
                        if e[0] == 'b':
                            self.modules['BackgroundsDrawer'].draw(e[1:], *p, *s)
                        elif e[0] == 'e':
                            self.modules['EnemyDrawer'].draw(
                                e[1:], *p, *s, self.pole)
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                PosX, PosY = event.pos
                print(PosX, PosY)
                if not errorFlag:
                    pass
            if event.type == pygame.MOUSEMOTION:
                PosX, PosY = event.pos
                if size[0]+pos[0] > PosX > pos[0] and size[1]+pos[1] > PosY > pos[1]:
                    PosX -= pos[0]
                    PosY -= pos[1]
                    PosX = PosX//(size[0]//16)
                    PosY = PosY//(size[1]//16)
                    errorPoint = (self.GetCoord(PosX), self.GetCoord(PosY))
                    if math.sqrt(abs(PosX - hodingPoint[0]) ** 2 + abs(PosY - hodingPoint[1]) ** 2) < 5:
                        errorFlag = False
                    else:
                        errorFlag = True

