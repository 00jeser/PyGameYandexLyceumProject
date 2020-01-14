import pygame
import GameObject
import math

size = (800, 800)
pos = (100, 100)

hod = 0  # 0-player 1-hoding 2-enemy
lastHod = 2
hoding = 0
moovingEnemy = ''
moovingCoords = [(0,0),(10,10)]
hodingPoint = (0, 0)
errorFlag = True
playerHodN,  enemyHodN = 0, 0
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
        self.playerEntity = []
        self.EnemyEntity = []

    def GetCoord(self, a):
        return a * (size[0]//16) + pos[0]

    def GetCoords(self, a):
        return (self.GetCoord(a[0]), self.GetCoord(a[1]))

    def GetCell(self, n):
        return (n - pos[0]) // (size[0]//16)

    def GetCells(self, n):
        return (self.GetCell(n[0]), self.GetCell(n[1]))

    def render(self, events):
        global hod 
        global hoding
        global hodingPoint
        global errorFlag
        global errorPoint
        global moovingEnemy
        global moovingCoords
        global lastHod
        global playerHodN
        global enemyHodN
        for i in range(16):
            for ii in range(16):
                p = self.GetCoords((i, ii))
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
                        self.modules['BackgroundsDrawer'].draw(
                            e[1:], *p, *s)
                    elif e[0] == 'e':
                        self.modules['EnemyDrawer'].draw(
                            e[1:], *p, *s, self.pole)
        if hod == 1:
            if moovingCoords[0][0] > moovingCoords[1][0]:
                moovingCoords[0] = (moovingCoords[0][0] - 1, moovingCoords[0][1])
            elif moovingCoords[0][0] < moovingCoords[1][0]:
                moovingCoords[0] = (moovingCoords[0][0] + 1, moovingCoords[0][1])
            if moovingCoords[0][1] > moovingCoords[1][1]:
                moovingCoords[0] = (moovingCoords[0][0], moovingCoords[0][1] - 1)
            elif moovingCoords[0][1] < moovingCoords[1][1]:
                moovingCoords[0] = (moovingCoords[0][0], moovingCoords[0][1] + 1)
            self.modules['EnemyDrawer'].draw(moovingEnemy[1:], *moovingCoords[0], *(50, 50), self.pole)
            if moovingCoords[0] == moovingCoords[1]:
                hoding -= 1
                if hoding <= 0:
                    coords = self.GetCells(moovingCoords[0])
                    self.pole[coords[0]][coords[1]].append(moovingEnemy)
                    if lastHod == 0:
                        enemyHodN += 1
                        if enemyHodN >= len(self.EnemyEntity):
                            enemyHodN = 0
                        hodingPoint = self.EnemyEntity[enemyHodN]
                        hod = 2
                    else:
                        playerHodN += 1
                        if playerHodN >= len(self.playerEntity):
                            playerHodN = 0
                        hodingPoint = self.playerEntity[playerHodN]
                        hod = 0
        elif hod == 2:
            hod = 1
            lastHod = 2
            hoding = 100
            hodingPoint = self.EnemyEntity[enemyHodN]
            moovingEnemy = self.pole[hodingPoint[0]][hodingPoint[1]][-1]
            moovingCoords = [self.GetCoords(hodingPoint), self.GetCoords((hodingPoint[0] - 1, hodingPoint[1]))]
            self.EnemyEntity[enemyHodN] = (hodingPoint[0] - 1, hodingPoint[1])
            self.pole[hodingPoint[0]][hodingPoint[1]] = self.pole[hodingPoint[0]][hodingPoint[1]][:-1]
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                PosX, PosY = self.GetCells(event.pos)
                if hod == 0:
                    if not errorFlag:
                        moovingEnemy = self.pole[hodingPoint[0]][hodingPoint[1]][-1]
                        #print(hodingPoint, self.pole[hodingPoint[0]][hodingPoint[1]])
                        self.pole[hodingPoint[0]][hodingPoint[1]] = self.pole[hodingPoint[0]][hodingPoint[1]][:-1]
                        moovingCoords = [self.GetCoords(hodingPoint), self.GetCoords((PosX, PosY))]
                        hoding = 100
                        hod = 1
                        lastHod = 0
                        self.playerEntity[playerHodN] = (PosX, PosY)


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

