import pygame
import headpiece
import levelManeger
import Backgrounds
import Enemys
import GameObject


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
FPS = 120
clock = pygame.time.Clock()

GameObject.openLvl = int(open('data.save', 'r').read())

for i in modules.keys():
    modules[i].init(modules)

while running:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 255, 0))
    for i in modules.keys():
        modules[i].render(ev)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
