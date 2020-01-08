import pygame
import headpiece
import levelManeger


running = True
screen = pygame.display.set_mode((500, 500))

head = headpiece.headpiece(screen)
level = levelManeger.levelManeger(screen)
modules = {
    'levelManeger': level,
    'headpiece': head
}
FPS = 120
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
