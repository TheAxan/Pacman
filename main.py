import pygame
import sys
import settings
import screen
import classes
import maps


pygame.init()


timer: int = 0
clock = pygame.time.Clock()

sprite_update = pygame.event.custom_type()
pygame.time.set_timer(sprite_update, 100)

pygame.key.set_repeat(15)

point_count: int = -settings.pellet_value
ate_pellet = pygame.event.custom_type()

def chase_switch(duration):
    global timer
    
    if timer > duration:
        classes.Ennemy.chase_mode = not classes.Ennemy.chase_mode
        for ennemy in classes.Ennemy.ennemies:
            ennemy.turn_around()
        timer = 0


while True:
    for event in pygame.event.get():
        if event.type == sprite_update:
            for entity in classes.Entity.entities:
                entity.sprite_next()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN):
                classes.pak.input_assignement(event.key)
            elif event.key is pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()

    screen.screen.blit(screen.background, (0, 0))  # reset background

    if maps.default_map.modified:
        maps.default_map.sprite_update()
        point_count += settings.pellet_value
    
    if classes.Ennemy.game_over:
        print(f'Score: {point_count}')
        sys.exit()
    
    maps.default_map.graphic_update()

    for entity in classes.Entity.entities:
        entity.routine()
    
    if settings.display_targets:
        for entity in classes.Ennemy.ennemies:
            entity.target_display()

    pygame.display.flip()

    clock.tick(60)
    timer += clock.get_time()
    
    if classes.Ennemy.chase_mode:
        chase_switch(settings.chase_duration)
    else:
        chase_switch(settings.scatter_duration)
