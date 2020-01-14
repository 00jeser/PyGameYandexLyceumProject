import pygame
import headpiece
import levelManeger
import Backgrounds
import Enemys


running = True
screen = pygame.display.set_mode((1000, 1000))


head = headpiece.headpiece(screen)
level = levelManeger.levelManeger(screen)
drawer0 = Backgrounds.BackgroundsDrawer(screen)
drawer1 = Enemys.EnemyDrawer(screen)
modules = {
    'levelManeger': level,
    'headpiece': head,
    'BackgroundsDrawer': drawer0,
    'EnemyDrawer': drawer1
}
FPS = 30
clock = pygame.time.Clock()

for i in modules.keys():
    modules[i].init(modules)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 255, 0))
    for i in modules.keys():
        modules[i].render(pygame.event.get())
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
