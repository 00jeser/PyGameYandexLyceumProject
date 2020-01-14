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
        self.screen.blit(self.enemys[n[1:-2]], (x, y, sx, sy))
        text_to_screen(self.screen, n[-2:], x + 15, y + 20, size=25)
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

def text_to_screen(screen, text, x, y, size = 50, color = (200, 000, 000), font_type = 'Comic Sans MS'):
        myfont = pygame.font.SysFont(font_type, size)
        textsurface = myfont.render(text, True, color)
        screen.blit(textsurface, (x, y))