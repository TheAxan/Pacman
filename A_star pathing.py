import pygame
from random import randrange
from tools import create_empty_array, print_array
from sys import exit

pygame.init()

u = 30

array_size = 20

white = 255, 255, 255
orange = 255, 153, 0
cyan = 0, 230, 230
black = 0,0,0
transparent = 0,0,0,0

screen = pygame.display.set_mode((array_size * u, array_size * u), flags=pygame.NOFRAME)
background = pygame.Surface((array_size * u, array_size * u))

outer_square = pygame.Surface((u, u))
outer_square.fill(white)
pygame.draw.rect(outer_square, black, (0, 0, u, u), 2)

black_square = pygame.Surface((u, u))
black_square.fill(black)

while True:
    array = create_empty_array(array_size, array_size)

    for row in array:
        for _ in range(randrange(int(array_size/3))):
            while True:
                position = randrange(array_size)
                if row[position] == 0:
                    row[position] = 1
                    break
    
    for axis in (x, y):
        for point in (origin, end):
            point.axis = randrange(array_size)
    
    for point, value in ((origin, 2), (end, 3)):
        array[point.y][point.y] = value
    
    for y_counter, row in enumerate(array):
        for x_counter, cell in enumerate(row):
            background.blit(outer_square, (x_counter * u, y_counter * u))
            if array[y_counter][x_counter] == 1:
                background.blit(black_square, (x_counter * u, y_counter * u))

    screen.blit(background, (0,0))

    reset_array = False
    while not reset_array:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key is pygame.K_ESCAPE:
                    exit()
                if event.key is pygame.K_BACKSPACE:
                    reset_array = True
                    # TODO verify if it effectively breaks from nested loop (nearest while true)
                    # (which appears to not actually be a nested loop, those being for i in list: for j in list2:)
            elif event.type == pygame.QUIT:
                exit()
        
        pygame.display.flip()
