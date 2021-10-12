import pygame
import sys
import screen_setup
import map_setup
import classes_setup


pygame.init()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN):
                classes_setup.pak.input_handling(event.key)
            elif event.key is pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()

    screen_setup.screen.blit(map_setup.background, (0, 0))  # reset background
    for entity in classes_setup.Entity.entities:
        entity.routine()
    clock.tick(60)
    pygame.display.flip()
