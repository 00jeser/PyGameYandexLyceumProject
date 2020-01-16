import pygame
import GameObject
import os


class EnemyDrawer(GameObject.GameObject):
    def __init__(self, screen):
        self.screen = screen
        self.enemys = {
            'y': load_image('yandex.png'),
            'yAlis': load_image('yandexAlisa.png'),
            'yAur': load_image('yandexAura.png'),
            'yBrow': load_image('yandexBrowser.png'),
            'yDisk': load_image('yandexDisk.png'),
            'yEda': load_image('yandexEda.png'),
            'yEfir': load_image('yandexEfir.png'),
            'yGame': load_image('yandexIgry.png'),
            'yMap': load_image('yandexKarti.png'),
            'yKP': load_image('yandexKinoPoisk.png'),
            'yMarket': load_image('yandexMarket.png'),
            'yMusic': load_image('yandexMuzika.png'),
            'yTrans': load_image('yandexPerevod.png'),
            'yPlus': load_image('yandexPlus.png'),
            'yMail': load_image('yandexPochta.png'),
            'yRadio': load_image('yandexRadio.png'),
            'yVid': load_image('yandexVideo.png'),
            'yZen': load_image('yandexZen.png'),
            'yTaxi': load_image('yandxTaxi.png'),
            'g': load_image('google.png'),
            'gAsist': load_image('googleAsistent.png'),
            'gChrome': load_image('googleChrome.png'),
            'gDisk': load_image('googleDisk.png'),
            'gMap': load_image('googleKarti.png'),
            'gMusic': load_image('googleMusic.png'),
            'gNews': load_image('googleNews.png'),
            'gTrans': load_image('googlePerevod.png'),
            'gPlus': load_image('googlePlus.png'),
            'gMail': load_image('googlePochta.png'),
            'gStadia': load_image('googleStadia.png'),
            'gYoutube': load_image('googleYoutube.png'),
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


def text_to_screen(screen, text, x, y, size=50, color=(10, 200, 000), font_type='Comic Sans MS'):
    myfont = pygame.font.SysFont(font_type, size)
    textsurface = myfont.render(text, True, color)
    screen.blit(textsurface, (x, y))
