import pygame
from sys import exit
from setup import pac, screen, background, entities

pygame.init()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN):
                pac.input = {
                    pygame.K_LEFT: (-pac.speed, 0),
                    pygame.K_UP: (0, -pac.speed),
                    pygame.K_RIGHT: (pac.speed, 0),
                    pygame.K_DOWN: (0, pac.speed),
                }[event.key]
            elif event.key is pygame.K_ESCAPE:
                exit()
        elif event.type == pygame.QUIT:
            exit()

    screen.blit(background, (0, 0))  # reset background
    for entity in entities:
        entity.routine()
    clock.tick(60)
    pygame.display.flip()
