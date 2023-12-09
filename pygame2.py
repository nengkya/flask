import pygame

display = pygame.display.set_mode((1280, 750))
clock = pygame.time.Clock()
running = True
player_position = pygame.Vector2(display.get_width() / 2, display.get_height() / 2)
delta_time = 0

while running:
    for event in pygame.event.get(): #must, so can get quit without Ctrl-C
        if event.type == pygame.QUIT:
            running = False

    display.fill((55, 77, 88));

    pygame.draw.circle(display, (43, 21, 87), player_position, 40)

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        if player_position.y < 0:
            player_position.y = display.get_height()
        player_position.y -= 300 * delta_time
    
    if key[pygame.K_s]:
        if player_position.y > display.get_height():
            player_position.y = 0
        player_position.y += 300 * delta_time

    if key[pygame.K_a]:
        if player_position.x < 0:
            player_position.x = display.get_width()
        player_position.x -= 300 * delta_time
        
    pygame.display.flip()

    delta_time = clock.tick(60) / 1000













