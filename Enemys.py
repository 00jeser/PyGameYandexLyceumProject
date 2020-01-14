import pygame
import GameObject
import os


class EnemyDrawer(GameObject.GameObject):
    def __init__(self, screen):
        self.screen = screen
        self.enemys = {
            'y': load_image('y.png')
        }


    def draw(self, n, x, y, sx, sy, pole):
        self.screen.blit(self.enemys[n[1:]], (x, y, sx, sy))
        #pygame.draw.rect(self.screen, (50, 0, 0, 0), (x, y, sx, sy), 1)


def load_image(name, colorkey=None):
    fullname = os.path.join('data\\imgs\\e', name)
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