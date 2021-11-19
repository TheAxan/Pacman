import pygame
from maps import default_map as map_grid


map_width = len(map_grid[0])
map_height = len(map_grid)

cu = 8
screen = pygame.display.set_mode((map_width * cu, map_height * cu), pygame.SCALED)
gu = cu * 2
# gu is short for graphical_unit, cu for cell_unit
# the long names would make most functions absurdly long (especially for gu drawings)  NOTE gu might be rendered obsoletet by sprites
pygame.display.set_caption('Pacman')
pygame.display.set_icon(pygame.image.load('img\pac2.png'))  # TODO switch this to east facing

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
pygame.draw.rect(square, black, (0, 0, cu, cu), (cu//8)*6)

for y_counter, row in enumerate(map_grid):
    for x_counter, cell in enumerate(row):
        if cell == 1:
            background.blit(square, (x_counter * cu, y_counter * cu)) # This draws the map
