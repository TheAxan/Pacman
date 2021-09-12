import pygame
import sys

pygame.init()

# basic grid map generation

map_grid = [[0 for x in range(28)] for x in range(31)]      # create empty array, 0 is empty cell

for i in (0, 2, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30):     # mostly filled horizontal lines
    map_grid[i] = [1 for x in range(28)]

for i in (0, 4, 5, 7, 8, 13, 14, 19, 20, 22, 23, 27):   # mostly filled vertical lines
    for x in map_grid:
        x[i] = 1

for i in map_grid:      # print map
    print(i)

# map display

size_mod = 3
u = 10 * size_mod

screen = pygame.display.set_mode([28 * u, 31 * u])
white = 255, 255, 255
yellow = 255, 255, 0
blue = 0, 0, 255
black = 0, 0, 0

square = pygame.Surface((u, u))
square.fill(blue)

y_counter = 0

for i in map_grid:
    x_counter = 0
    for x in i:
        if x:
            screen.blit(square, (x_counter * u, y_counter * u))
        x_counter += 1
    y_counter += 1

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
