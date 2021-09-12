import sys, pygame
from math import pi
pygame.init()

screen = pygame.display.set_mode([1000, 1000])
white = 255, 255, 255
yellow = 255, 255, 0
blue = 0, 0, 255
black = 0, 0, 0

pygame.draw.rect(screen, white, (200, 0, 600, 800), 3)

pygame.draw.line(screen, blue, (460, 380), (540, 380))
pygame.draw.line(screen, blue, (440, 419), (560, 419))

pygame.draw.circle(screen, yellow, (500, 400), 18)
pygame.draw.polygon(screen, black, ((500, 400), (481, 381), (481, 419)))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

# size = width, height = 1000, 1000
# speed = [1, 1]
# black = 0, 0, 0
#
# screen = pygame.display.set_mode(size)
#
# ball = pygame.image.load("intro_ball.gif")
# ballrect = ball.get_rect()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()