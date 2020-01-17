
import GameObject
import pygame
import random


class MenuLevel(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.colorBtn1 = (255, 215, 0)
        self.colorBtn2 = (255, 215, 0) # Кнопка "выход"
        self.colorBtn3 = (255, 215, 0)
        self.colorBtn4 = (255, 215, 0)
        self.colorBtn5 = (255, 215, 0)
        self.colorBtn6 = (255, 215, 0)
        self.colorBtn7 = (255, 215, 0)

    def render(self, events):
        if self.modules['headpiece'].timer < 195:
            return
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, 5000, 5000), 0)
        pygame.draw.rect(self.screen, self.colorBtn1, (205, 110, 300, 100), 0)
        pygame.draw.rect(self.screen, self.colorBtn2, (370, 470, 300, 100), 0) # Кнопка "выход"
        pygame.draw.rect(self.screen, self.colorBtn3, (535, 110, 300, 100), 0)
        pygame.draw.rect(self.screen, self.colorBtn4, (205, 230, 300, 100), 0)
        pygame.draw.rect(self.screen, self.colorBtn5, (535, 230, 300, 100), 0)
        pygame.draw.rect(self.screen, self.colorBtn6, (205, 350, 300, 100), 0)
        pygame.draw.rect(self.screen, self.colorBtn7, (535, 350, 300, 100), 0)

        myfont = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont.render('Уровень 1', True, (0, 0, 0))
        self.screen.blit(textsurface, (215, 110))

        myfont = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont.render('Уровень 2', True, (0, 0, 0))
        self.screen.blit(textsurface, (545, 110))

        myfont = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont.render('Уровень 3', True, (0, 0, 0))
        self.screen.blit(textsurface, (215, 230))

        myfont = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont.render('Уровень 4', True, (0, 0, 0))
        self.screen.blit(textsurface, (545, 230))

        myfont = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont.render('Уровень 5', True, (0, 0, 0))
        self.screen.blit(textsurface, (215, 350))

        myfont = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont.render('Уровень 6', True, (0, 0, 0))
        self.screen.blit(textsurface, (545, 350))

        myfont = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont.render('Выход', True, (0, 0, 0))
        self.screen.blit(textsurface, (420, 470))

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                pressed = pygame.mouse.get_pressed()
                PosX, PosY = event.pos
                if ((205 < PosX and PosX < 505) and (110 < PosY and PosY < 210)):
                    self.colorBtn1 = (80, 80, 80)
                    self.modules["levelManeger"].setLevel(1, 1)
                if ((535 < PosX and PosX < 835) and (110 < PosY and PosY < 210)):
                    self.colorBtn3 = (80, 80, 80)
                    self.modules["levelManeger"].setLevel(1, 2)
                if ((205 < PosX and PosX < 505) and (230 < PosY and PosY < 330)):
                    self.colorBtn4 = (80, 80, 80)
                    self.modules["levelManeger"].setLevel(1, 3)
                if ((535 < PosX and PosX < 835) and (230 < PosY and PosY < 330)):
                    self.colorBtn5 = (80, 80, 80)
                    self.modules["levelManeger"].setLevel(1, 4)
                if ((205 < PosX and PosX < 505) and (350 < PosY and PosY < 450)):
                    self.colorBtn6 = (80, 80, 80)
                    self.modules["levelManeger"].setLevel(1, 5)
                if ((535 < PosX and PosX < 835) and (350 < PosY and PosY < 450)):
                    self.colorBtn7 = (80, 80, 80)
                    self.modules["levelManeger"].setLevel(1, random.randint(6, 7))
                if ((370 < PosX and PosX < 670) and (470 < PosY and PosY < 570)):
                    self.colorBtn2 = (80, 80, 80)
                    exit()

            if event.type == pygame.MOUSEMOTION:
                PosX, PosY = event.pos
                if ((205 < PosX and PosX < 505) and (110 < PosY and PosY < 210)):
                    self.colorBtn1 = (218, 165, 32)
                else:
                    self.colorBtn1 = (255, 215, 0)
                if ((535 < PosX and PosX < 835) and (110 < PosY and PosY < 210)):
                    self.colorBtn3 = (218, 165, 32)
                else:
                    self.colorBtn3 = (255, 215, 0)
                if ((205 < PosX and PosX < 505) and (230 < PosY and PosY < 330)):
                    self.colorBtn4 = (218, 165, 32)
                else:
                    self.colorBtn4 = (255, 215, 0)
                if ((535 < PosX and PosX < 835) and (230 < PosY and PosY < 330)):
                    self.colorBtn5 = (218, 165, 32)
                else:
                    self.colorBtn5 = (255, 215, 0)
                if ((205 < PosX and PosX < 505) and (350 < PosY and PosY < 450)):
                    self.colorBtn6 = (218, 165, 32)
                else:
                    self.colorBtn6 = (255, 215, 0)
                if ((535 < PosX and PosX < 835) and (350 < PosY and PosY < 450)):
                    self.colorBtn7 = (218, 165, 32)
                else:
                    self.colorBtn7 = (255, 215, 0)
                if ((370 < PosX and PosX < 670) and (470 < PosY and PosY < 570)):
                    self.colorBtn2 = (218, 165, 32)
                else:
                    self.colorBtn2 = (255, 215, 0)