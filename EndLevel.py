import pygame
import GameObject
from Enemys import text_to_screen

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
        pygame.draw.polygon(self.screen, (255, 215, 0), [(200,480),(700,480),(700,520),(200,520)], 3)
        pygame.draw.polygon(self.screen, (255, 215, 0), [(700,520),(800,520),(810,500),(800,480),(700, 480)])
        if self.win:
            text_to_screen(self.screen, "Вы выиграли", 220, 485, size=25, color=(0,0,0), font_type='Arial')
        else:
            text_to_screen(self.screen, "Вы проиграли", 220, 485, size=25, color=(0,0,0), font_type='Arial')
        text_to_screen(self.screen, "Далее", 710, 485, size=25, color=(0,0,0), font_type='Arial')
        

