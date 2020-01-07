import pygame


running = True
screen = pygame.display.set_mode((500, 500))

modules = {}

for i in modules:
    i.init(modules)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for i in modules:
        i.render(pygame.event.get())
    pygame.display.flip()
pygame.quit()