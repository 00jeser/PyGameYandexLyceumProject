import pygame
import headpiece


running = True
screen = pygame.display.set_mode((500, 500))

head = headpiece.headpiece(screen)
modules = {'headpiece':head}
FPS = 50
clock = pygame.time.Clock()

for i in modules.keys():
    modules[i].init(modules)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for i in modules.keys():
        modules[i].render(pygame.event.get())
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()