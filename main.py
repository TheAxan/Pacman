import pygame
import sys
import setup

pygame.init()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN):
                setup.pak.input = {
                    pygame.K_LEFT: (-setup.pak.speed, 0),
                    pygame.K_UP: (0, -setup.pak.speed),
                    pygame.K_RIGHT: (setup.pak.speed, 0),
                    pygame.K_DOWN: (0, setup.pak.speed),
                }[event.key]
            elif event.key is pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()

    setup.screen.blit(setup.background, (0, 0))  # reset background
    for entity in setup.Entity.entities:
        entity.routine()
    clock.tick(60)
    pygame.display.flip()
