import sys, pygame

size = width, height = 400, 500
display =  pygame.display.set_mode(size)
speed = [2, 2]
ball = pygame.image.load('intro_ball.gif')
ball_get_rectangle = ball.get_rect()
print(ball_get_rectangle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() #clean exit, no error message in terminal

    ball_get_rectangle.move(speed)

    if ball_get_rectangle.left < 0 or ball_get_rectangle.right > width:
        speed[0] = -speed[0]

    display.fill((111, 222, 44))
    display.blit(ball, ball_get_rectangle) #draw ball into display
    pygame.display.flip()
