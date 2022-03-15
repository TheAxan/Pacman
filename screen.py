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

background = pygame.Surface((current_map.width * cu, current_map.height * cu))
for y_counter, row in enumerate(current_map.walls):
    for x_counter, cell in enumerate(row):
        if cell == 1:
            background.blit(square, (x_counter * cu + cu/2, y_counter * cu + cu/2)) # This draws the current_map
