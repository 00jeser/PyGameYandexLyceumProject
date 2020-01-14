
import GameObject
import pygame


class MenuLevel(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.colorBtn1 = (20, 30, 40)
        self.colorBtn2 = (20, 30, 40)

    def render(self, events):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 5000, 5000), 0)
        pygame.draw.rect(self.screen, self.colorBtn1, (10, 50, 150, 50), 0)
        pygame.draw.rect(self.screen, self.colorBtn2, (10, 110, 150, 50), 0)

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Игра', True, (255, 255, 255, 255))
        self.screen.blit(textsurface, (11, 50))

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Выход', True, (255, 255, 255, 255))
        self.screen.blit(textsurface, (11, 110))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = pygame.mouse.get_pressed()
                PosX, PosY = event.pos
                if ((10 < PosX and PosX < 160) and (50 < PosY and PosY < 100)):
                    self.colorBtn1 = (80, 80, 80)
                    self.modules["levelManeger"].setLevel(1, 0)
                if ((10 < PosX and PosX < 160) and (110 < PosY and PosY < 160)):
                    self.colorBtn2 = (80, 80, 80)
                    exit()

            if event.type == pygame.MOUSEMOTION:
                PosX, PosY = event.pos
                if ((10 < PosX and PosX < 160) and (50 < PosY and PosY < 100)):
                    self.colorBtn1 = (40, 40, 40)
                else:
                    self.colorBtn1 = (20, 30, 40)
                if ((10 < PosX and PosX < 160) and (110 < PosY and PosY < 160)):
                    self.colorBtn2 = (40, 40, 40)
                else:
                    self.colorBtn2 = (20, 30, 40)
