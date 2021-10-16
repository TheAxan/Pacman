import pygame
import sys
import screen
import classes


pygame.init()
clock = pygame.time.Clock()
display_targets: bool = False
timer: int = 0
chase_duration: int = 20000
scatter_duration: int = 7000

def chase_switch(duration):
    global timer
    
    if timer > duration:
        classes.Ennemy.chase_mode = not classes.Ennemy.chase_mode
        for ennemy in classes.Ennemy.ennemies:
            ennemy.turn_around()
        timer = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN):
                classes.pak.input_assignement(event.key)
            elif event.key is pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()

    screen.screen.blit(screen.background, (0, 0))  # reset background
    for entity in classes.Entity.entities:
        entity.routine()
    if display_targets:
        for entity in classes.Ennemy.ennemies:
            entity.targeting_display()
    clock.tick(60)
    timer += clock.get_time()
    if classes.Ennemy.chase_mode:
        chase_switch(chase_duration)
    else:
        chase_switch(scatter_duration)
    pygame.display.flip()
