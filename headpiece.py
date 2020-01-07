import GameObject
import pygame


class headpiece(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.timer = 0
        pygame.font.init()

    def render(self, events):
        self.timer -= -1

        if (self.timer < 100):
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render('Гавриленко Сергей', True, (255, 255, 255, 255))
            self.screen.blit(textsurface,(0,0))

            myfont1 = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont1.render('и', False, (255, 255, 255))
            self.screen.blit(textsurface,(90,30))
            
            myfont2 = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont2.render('Марданов Тимур', False, (255, 255, 255))
            self.screen.blit(textsurface,(0,60))
        elif(self.timer < 200):
            myfont3 = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont3.render('представляют', False, (255, 255, 255))
            self.screen.blit(textsurface,(0,0))
    
