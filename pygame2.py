import pygame

display = pygame.display.set_mode((1280, 750))
running = True

while running:
    for event in pygame.event.get(): #must, so can get quit without Ctrl-C
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
