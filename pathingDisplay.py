import pygame
import random
import tools
import sys


pygame.init()

u = 4

array_size = 250

white = 255, 255, 255
black = 0,0,0
orange = 255, 153, 0, 120 # explored
cyan = 0, 230, 230, 120 # to explore
green = 0, 255, 0 # origin
red = 255, 0, 0 # goal

screen = pygame.display.set_mode((array_size * u, array_size * u), flags=pygame.NOFRAME)
background = pygame.Surface((array_size * u, array_size * u))

def create_square(color, alpha=255):
    square = pygame.Surface((u, u))
    square.fill(color)
    square.set_alpha(alpha)
    return square

black_square = create_square(black)
orange_square = create_square(orange, 120)
cyan_square = create_square(cyan, 120)
outer_square = create_square(white)
# pygame.draw.rect(outer_square, black, (0, 0, u, u), 1)

arial = pygame.freetype.SysFont('arial', 10)

random_array = tools.create_empty_array(array_size, array_size)

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


# randomly set origin and end
origin = (random.randrange(array_size), random.randrange(array_size))
end = (random.randrange(array_size), random.randrange(array_size))

for point, value in ((origin, 2), (end, 3)):
    random_array[point[1]][point[0]] = value

# randomly place walls
for row in random_array:
    for _ in range(int(array_size * 0.2)):
        while True:
            position = random.randrange(array_size)
            if row[position] == 0:
                row[position] = 1
                break

# make background
for y_counter, row in enumerate(random_array):
    for x_counter, cell in enumerate(row):
        background.blit(outer_square, (x_counter * u, y_counter * u))
        if random_array[y_counter][x_counter] == 1:
            background.blit(black_square, (x_counter * u, y_counter * u))

screen.blit(background, (0,0))
screen.blit(create_square(green, 120), (origin[0] * u, origin[1] * u))
screen.blit(create_square(red, 120), (end[0] * u, end[1] * u))
