
import GameObject
import pygame


class MenuLevel(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.colorBtn1 = (255, 215, 0)
        self.colorBtn2 = (255, 215, 0)

    def render(self, events):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 5000, 5000), 0)
        pygame.draw.rect(self.screen, self.colorBtn1, (355, 250, 300, 100), 0)
        pygame.draw.rect(self.screen, self.colorBtn2, (355, 400, 300, 100), 0)

        myfont = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont.render('Игра', True, (255, 255, 255, 255))
        self.screen.blit(textsurface, (434.58, 250))

        myfont = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont.render('Выход', True, (255, 255, 255, 255))
        self.screen.blit(textsurface, (405, 400))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = pygame.mouse.get_pressed()
                PosX, PosY = event.pos
                if ((355 < PosX and PosX < 655) and (250 < PosY and PosY < 350)):
                    self.colorBtn1 = (80, 80, 80)
                    self.modules["levelManeger"].setLevel(1, 0)
                if ((355 < PosX and PosX < 655) and (400 < PosY and PosY < 500)):
                    self.colorBtn2 = (80, 80, 80)
                    exit()

            if event.type == pygame.MOUSEMOTION:
                PosX, PosY = event.pos
                if ((355 < PosX and PosX < 655) and (250 < PosY and PosY < 350)):
                    self.colorBtn1 = (218, 165, 32)
                else:
                    self.colorBtn1 = (255, 215, 0)
                if ((355 < PosX and PosX < 655) and (400 < PosY and PosY < 500)):
                    self.colorBtn2 = (218, 165, 32)
                else:
                    self.colorBtn2 = (255, 215, 0)