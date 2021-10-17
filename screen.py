import pygame
from maps import default_map as map_grid


map_width = len(map_grid[0])
map_height = len(map_grid)

cu = 16 # TODO switch to 8 so as to scale the screen only and remove sprite scaling, NOTE: this requires a speed/move_ip system overhaul due to int rounding affecting speed and immobilizing at 8
screen = pygame.display.set_mode((map_width * cu, map_height * cu), pygame.SCALED)
gu = cu * 2
# gu is short for graphical_unit, cu for cell_unit
# the long names would make most functions absurdly long (especially for gu drawings)

white = 255, 255, 255
black = 0, 0, 0
dark_grey = 15, 15, 15
yellow = 255, 255, 0
blue = 0, 0, 255
red = 255, 0, 0
orange = 255, 153, 0
cyan = 0, 230, 230
pink = 255, 179, 255

background = pygame.Surface((map_width * cu, map_height * cu))

square = pygame.Surface((cu, cu))
square.fill(blue)
pygame.draw.rect(square, black, (0, 0, cu, cu), int(gu/2.5))

for y_counter, row in enumerate(map_grid):
    for x_counter, cell in enumerate(row):
        if cell == 1:
            background.blit(square, (x_counter * cu, y_counter * cu)) # This draws the map
