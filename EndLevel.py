import pygame
import GameObject

class EndLevel():
    def __init__(self, screen, level = 0, win = True):
        super().__init__()
        self.screen = screen
        if win:
            f = open('data.save', 'w')
            f.write(level + 1)
        self.win = win
    
    def render(self, events):
        pass
        

