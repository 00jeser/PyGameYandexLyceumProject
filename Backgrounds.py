import pygame
import GameObject
import random
import os

class BackgroundsDrawer(GameObject.GameObject):
    def __init__(self, screen):
        self.screen = screen
        self.fons = {
            'b': load_image('b.png'),
            'hL': load_image('horLine.png'),
            'vL': load_image('vertLine.png'),
            'k': load_image('klet.png'),
            'w': load_image('w.png'),
            'g': load_image('w.png'),
        }


    def draw(self, n, x, y, sx, sy):
        self.screen.blit(self.fons[n], (x, y, sx, sy))
        # print('I`m print', n, 'on', x, y, 'with size', sx, sy)


def load_image(name, colorkey=None):
    fullname = os.path.join('data\\imgs\\b', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не могу загрузить изображение:', name)
        raise SystemExit(message)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
