import pygame
import sys
pygame.init()

# display tests

# screen = pygame.display.set_mode([1000, 1000])
# white = 255, 255, 255
# yellow = 255, 255, 0
# blue = 0, 0, 255
# black = 0, 0, 0
#
# pygame.draw.rect(screen, white, (200, 0, 600, 800), 3)
#
# pygame.draw.line(screen, blue, (460, 380), (540, 380))
# pygame.draw.line(screen, blue, (440, 419), (560, 419))
#
# pygame.draw.circle(screen, yellow, (500, 400), 18)
# pygame.draw.polygon(screen, black, ((500, 400), (481, 381), (481, 419)))
#
#
# pygame.display.flip()




# 28x31 array, will have to use array[y][x]

map_grid = [[0 for x in range(28)] for x in range(31)]      # create empty array, 0 is empty cell

for i in (0, 2, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30):     # mostly filled horizontal lines
    map_grid[i] = [1 for x in range(28)]

for i in (0, 4, 5, 7, 8, 13, 14, 19, 20, 22, 23, 27):   # mostly filled vertical lines
    for x in map_grid:
        x[i] = 1

for i in map_grid:      # print map
    print(i)


# display map

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
