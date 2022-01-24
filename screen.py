import pygame
import settings
from maps import default_map as map


def scaled_option(toggle):
    if toggle:
        return pygame.SCALED
    else:
        return 0


cu = settings.cell_unit
gu = cu * 2  # Graphical Unit
screen = pygame.display.set_mode(
    (map.width * cu, map.height * cu),
    scaled_option(settings.scaling_toggle)
)

pygame.display.set_caption('Pacman')
pygame.display.set_icon(pygame.image.load('image_files\pac_right_2.png'))


square = pygame.Surface((cu/8, cu/8))
square.fill(settings.blue)

background = pygame.Surface((map.width * cu, map.height * cu))
for y_counter, row in enumerate(map.walls):
    for x_counter, cell in enumerate(row):
        if cell == 1:
            background.blit(square, (x_counter * cu + cu/2, y_counter * cu + cu/2)) # This draws the map
