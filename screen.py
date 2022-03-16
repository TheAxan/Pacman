import pygame
import settings
import maps


def scaled_option(toggle):
    if toggle:
        return pygame.SCALED
    else:
        return 0

current_map =  getattr(maps, settings.selected_map)

cu = settings.cell_unit
gu = cu * 2  # Graphical Unit
screen = pygame.display.set_mode(
    (current_map.width * cu, current_map.height * cu),
    scaled_option(settings.scaling_toggle)
)

pygame.display.set_caption('Pacman')
pygame.display.set_icon(pygame.image.load('image_files\pac_right_2.png'))


square = pygame.Surface((cu/8, cu/8))
square.fill(settings.blue)

wall_type_to_rotation = {
    1: 180,
    3: 90,
    5: 0,
    7: -90
}
outer_corner_type_to_rotation = {
    2: 90,
    4: 0,
    6: -90,
    8: 180
}
inner_corner_type_to_rotation = {
    10: 0,
    11: -90,
    12: 180,
    13: 90
}

background = pygame.Surface((current_map.width * cu, current_map.height * cu))
for y_counter, row in enumerate(current_map.wall_types):
    for x_counter, cell in enumerate(row):
        if cell == 0:
            continue
        elif cell in (1, 3, 5, 7): # walls
            square = pygame.image.load('image_files\wall.png')
            square = pygame.transform.rotate(square, wall_type_to_rotation[cell])
        elif cell in (2, 4, 6, 8): # outer corner
            square = pygame.image.load('image_files\outer_corner.png')
            square = pygame.transform.rotate(square, outer_corner_type_to_rotation[cell])
        elif cell in (10, 11, 12, 13): #inner corner
            square = pygame.image.load('image_files\inner_corner.png')
            square = pygame.transform.rotate(square, inner_corner_type_to_rotation[cell])
        
        background.blit(square, (x_counter * cu, y_counter * cu)) # This draws the current_map
