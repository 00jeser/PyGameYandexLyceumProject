import pygame
import GameObject
import random
import os

class BackgroundsDrawer(GameObject.GameObject):
    def __init__(self, screen):
        self.screen = screen
        self.fons = {
            'g': load_image('g.png'),
            'k': load_image('k.png')
        }


    def draw(self, n, x, y, sx, sy):
        self.screen.blit(self.fons[n], (x, y, sx, sy))
        pygame.draw.rect(self.screen, (50, 0, 0, 0), (x, y, sx, sy), 1)
        # print('I`m print', n, 'on', x, y, 'with size', sx, sy)


def load_image(name, colorkey=None):
    fullname = os.path.join('data\\imgs', name)
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
