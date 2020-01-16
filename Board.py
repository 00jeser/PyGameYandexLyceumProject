import pygame
import GameObject
import math

size = (800, 800)
pos = (100, 100)

hod = 0  # 0-player 1-hoding 2-enemy
lastHod = 2
hoding = 0
moovingEnemy = ''
moovingCoords = [(0, 0), (10, 10)]
hodingPoint = (10, 0)
errorFlag = True
playerHodN,  enemyHodN = 0, 0
errorPoint = (-100, -100)
attackFlag = False
attackPoint = (-1, -1)


class Board(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
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
        global attackFlag
        global attackPoint
        self.screen = screen
        self.pole = []
        self.levelN = 0
        for i in range(16):
            self.pole.append([])
            for _ in range(16):
                self.pole[i].append('')
        self.playerEntity = []
        self.EnemyEntity = []
        hod = 0  # 0-player 1-hoding 2-enemy
        lastHod = 2
        hoding = 0
        moovingEnemy = ''
        moovingCoords = [(0, 0), (10, 10)]
        hodingPoint = (0, 0)
        errorFlag = True
        playerHodN,  enemyHodN = 0, 0
        errorPoint = (-100, -100)
        attackFlag = False
        attackPoint = (-1, -1)
    
    def setHodingPoint(self):
        global hodingPoint
        hodingPoint = self.playerEntity[0]

    def GetCoord(self, a):
        return a * (size[0]//16) + pos[0]

    def GetCoords(self, a):
        return (self.GetCoord(a[0]), self.GetCoord(a[1]))

    def GetCell(self, n):
        return (n - pos[0]) // (size[0]//16)

    def GetCells(self, n):
        return (self.GetCell(n[0]), self.GetCell(n[1]))

    def render(self, events):
        pygame.draw.rect(self.screen, (255, 215, 0), (0, 0, 50, 50), 0)
        pygame.draw.line(self.screen, (0, 0, 0), (2, 2), (46, 46), 2)
        pygame.draw.line(self.screen, (0, 0, 0), (46, 2), (2, 46), 2)
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
        global attackFlag
        global attackPoint
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
                                         (*errorPoint, 50, 50), 1)
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
                moovingCoords[0] = (moovingCoords[0][0] -
                                    1, moovingCoords[0][1])
            elif moovingCoords[0][0] < moovingCoords[1][0]:
                moovingCoords[0] = (moovingCoords[0][0] +
                                    1, moovingCoords[0][1])
            if moovingCoords[0][1] > moovingCoords[1][1]:
                moovingCoords[0] = (moovingCoords[0][0],
                                    moovingCoords[0][1] - 1)
            elif moovingCoords[0][1] < moovingCoords[1][1]:
                moovingCoords[0] = (moovingCoords[0][0],
                                    moovingCoords[0][1] + 1)
            self.modules['EnemyDrawer'].draw(
                moovingEnemy[1:], *moovingCoords[0], *(50, 50), self.pole)
            if moovingCoords[0] == moovingCoords[1]:
                hoding -= 1
                if hoding <= 0:
                    coords = self.GetCells(moovingCoords[0])
                    self.pole[coords[0]][coords[1]].append(moovingEnemy)
                    if attackFlag:
                        s = max(int(moovingEnemy[-2:]) // 3, 1)
                        m = int(self.pole[attackPoint[0]]
                                [attackPoint[1]][-1][-2:])
                        print(s, m, moovingEnemy)
                        if m - s <= 0:
                            self.pole[attackPoint[0]][attackPoint[1]
                                                      ] = self.pole[attackPoint[0]][attackPoint[1]][:-1]
                            if lastHod == 0:
                                self.EnemyEntity.remove(attackPoint)
                            else:
                                self.playerEntity.remove(attackPoint)
                        else:
                            self.pole[attackPoint[0]][attackPoint[1]][-1] = self.pole[attackPoint[0]
                                                                                      ][attackPoint[1]][-1][:-2] + str(m - s).rjust(2, '0')
                    if lastHod == 0:
                        enemyHodN += 1
                        if enemyHodN >= len(self.EnemyEntity):
                            enemyHodN = 0
                        if len(self.EnemyEntity) == 0:
                            self.modules['levelManeger'].setLevel(2, (self.levelN, True))
                            return
                        hodingPoint = self.EnemyEntity[enemyHodN]
                        hod = 2
                    else:
                        playerHodN += 1
                        if playerHodN >= len(self.playerEntity):
                            playerHodN = 0
                        if len(self.playerEntity) == 0:
                            self.modules['levelManeger'].setLevel(2, (self.levelN, False))
                            return
                        hodingPoint = self.playerEntity[playerHodN]
                        hod = 0
        elif hod == 2:
            hod = 1
            lastHod = 2
            hoding = 100
            hodingPoint = self.EnemyEntity[enemyHodN]
            moovingEnemy = self.pole[hodingPoint[0]][hodingPoint[1]][-1]

            needPoint = (-2, -2)
            attackFlag = False
            minDis = 1000
            minE = (-1, -1)
            for i in self.playerEntity:
                dis = math.sqrt(abs(hodingPoint[0] - i[0])**2+abs(hodingPoint[1] - i[1])**2)
                if dis <= 5:
                    needPoint = self.findAttackPoint(*i, *hodingPoint)
                    if needPoint == (-1, -1):
                        needPoint = hodingPoint
                        attackFlag = False
                    else:
                        if minDis > dis:
                            minDis = dis
                            attackFlag = True
                            attackPoint = i 
            minDis = 1000
            if needPoint == (-2, -2):
                for i in self.playerEntity:
                    dis = math.sqrt(abs(hodingPoint[0] - i[0])**2+abs(hodingPoint[1] - i[1])**2)
                    if dis < minDis:
                        minDis = dis
                        minE = i
                minDis = 1000
                for x in range(-5, 6):
                    for y in range(-5, 6):
                        if math.sqrt(x**2 + y**2) < 5 and 0 <= hodingPoint[0]+x <= 15 and 0 <= hodingPoint[1]+y <= 15:
                            if self.pole[hodingPoint[0]+x][hodingPoint[1]+y][-1][0] != 'e':
                                dis = math.sqrt(abs(hodingPoint[0]+x - needPoint[0]) ** 2 + abs(hodingPoint[1]+y - needPoint[1]) ** 2)
                                if dis < minDis:
                                    minDis = dis
                                    needPoint = (hodingPoint[0]+x, hodingPoint[1]+y)
            moovingCoords = [self.GetCoords(
                hodingPoint), self.GetCoords(needPoint)]
            self.EnemyEntity[enemyHodN] = needPoint
            self.pole[hodingPoint[0]][hodingPoint[1]
                                      ] = self.pole[hodingPoint[0]][hodingPoint[1]][:-1]

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                posm = event.pos
                if posm[0] < 50 and posm[1] < 50:
                    self.modules['levelManeger'].setLevel(0)
                    return
                PosX, PosY = self.GetCells(posm)
                if hod == 0:
                    if not errorFlag:
                        if event.button == 1:
                            if self.pole[PosX][PosY][-1][0] == 'e':
                                needPoint = self.findAttackPoint(PosX, PosY, *hodingPoint)
                                if needPoint == (-1, -1):
                                    continue
                                moovingEnemy = self.pole[hodingPoint[0]
                                                        ][hodingPoint[1]][-1]
                                self.pole[hodingPoint[0]][hodingPoint[1]
                                                        ] = self.pole[hodingPoint[0]][hodingPoint[1]][:-1]
                                print(*needPoint)
                                moovingCoords = [self.GetCoords(
                                    hodingPoint), self.GetCoords(needPoint)]
                                hoding = 50
                                hod = 1
                                lastHod = 0
                                self.playerEntity[playerHodN] = needPoint
                                attackFlag = True
                                attackPoint = (PosX, PosY)
                            else:
                                moovingEnemy = self.pole[hodingPoint[0]
                                                        ][hodingPoint[1]][-1]
                                self.pole[hodingPoint[0]][hodingPoint[1]
                                                        ] = self.pole[hodingPoint[0]][hodingPoint[1]][:-1]
                                moovingCoords = [self.GetCoords(
                                    hodingPoint), self.GetCoords((PosX, PosY))]
                                hoding = 50
                                hod = 1
                                lastHod = 0
                                self.playerEntity[playerHodN] = (PosX, PosY)
                                attackFlag = False
                        elif event.button == 3:
                            moovingEnemy = self.pole[hodingPoint[0]
                                                    ][hodingPoint[1]][-1]
                            self.pole[hodingPoint[0]][hodingPoint[1]
                                                    ] = self.pole[hodingPoint[0]][hodingPoint[1]][:-1]
                            moovingCoords = [self.GetCoords(hodingPoint), self.GetCoords(hodingPoint)]
                            hoding = 50
                            hod = 1
                            lastHod = 0
                            self.playerEntity[playerHodN] = hodingPoint
                            attackFlag = False


            if event.type == pygame.MOUSEMOTION:
                PosX, PosY = event.pos
                if size[0]+pos[0] > PosX > pos[0] and size[1]+pos[1] > PosY > pos[1]:
                    PosX, PosY = self.GetCells((PosX, PosY))
                    errorPoint = (self.GetCoord(PosX), self.GetCoord(PosY))
                    if math.sqrt(abs(PosX - hodingPoint[0]) ** 2 + abs(PosY - hodingPoint[1]) ** 2) < 10:
                        errorFlag = False
                    else:
                        errorFlag = True

    def findAttackPoint(self, xObj, yObj, xSource, ySource):
        if abs(xObj - xSource) <= 1 and abs(yObj - ySource) <= 1:
            return xSource, ySource
        minDis = 1000
        minPoint = (-1, -1)
        for i in range(-1, 2):
            for ii in range(-1, 2):
                point = (xObj + i, yObj + ii)
                if point[0] < 0 or point[0] > 15 or point[1] < 0 or point[1] > 15 or i == ii == 0 or self.pole[point[0]][point[1]][-1][0] == 'e':
                    pass
                else:
                    print('calk for', *point)
                    dis = math.sqrt(
                        abs(point[0] - xSource) ** 2 + abs(point[1] - ySource) ** 2)
                    print('dis =', dis)
                    if minDis > dis:
                        print('its less')
                        minDis = dis
                        minPoint = point
        return minPoint
