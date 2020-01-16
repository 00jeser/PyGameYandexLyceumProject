import pygame
import GameObject

class EndLevel(GameObject.GameObject):
    def __init__(self, screen, level = 0, win = False):
        super().__init__()
        self.screen = screen
        if win:
            f = open('data.save', 'w')
            f.write(str(level + 1))
        self.win = win
    
    def render(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                self.modules['levelManeger'].setLevel(0)
        self.screen.fill((255, 255, 255))
        

