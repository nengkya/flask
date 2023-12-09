#initialize all imported pygame modules
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720)) #tuple unchangeable
clock  = pygame.time.Clock() #create a clock object which can be used to keep track of time
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')

    pygame.display.flip() #update the display surface to the screen
