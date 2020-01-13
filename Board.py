import pygame
import GameObject

size = (800, 800)
pos = (100, 100)


class Board(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.pole = []
        for i in range(16):
            self.pole.append([])
            for _ in range(16):
                self.pole[i].append('')

    def render(self, events):
        for i in range(16):
            for ii in range(16):
                p = (size[0]//16*i+pos[0], size[1]//16*ii+pos[1])
                s = (size[0]//16, size[1]//16)
                for e in self.pole[i][ii]:
                    if e[0] == 'b':
                        self.modules['BackgroundsDrawer'].draw(e[1], *p, *s)
