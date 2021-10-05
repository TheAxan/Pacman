import pygame
from random import randrange
from tools import create_empty_array
from sys import exit

pygame.init()

u = 30

array_size = 20

white = 255, 255, 255
black = 0,0,0
orange = 255, 153, 0, 120 # explored
cyan = 0, 230, 230, 120 # to explore
green = 0, 255, 0, 120 # origin
red = 255, 0, 0, 120 # goal

screen = pygame.display.set_mode((array_size * u, array_size * u), flags=pygame.NOFRAME)
background = pygame.Surface((array_size * u, array_size * u))

outer_square = pygame.Surface((u, u))
outer_square.fill(white)
pygame.draw.rect(outer_square, black, (0, 0, u, u), 2)

def square(color):
    colored_square = pygame.Surface((u, u))
    colored_square.fill(color)
    return colored_square
black_square = square(black)

while True:
    array = create_empty_array(array_size, array_size)

    origin = {'x': randrange(array_size), 'y': randrange(array_size)}
    end = {'x': randrange(array_size), 'y': randrange(array_size)}
    
    for point, value in ((origin, 2), (end, 3)):
        array[point['x']][point['y']] = value
    
    for row in array:
        for _ in range(int(array_size * 0.2)):
            while True:
                position = randrange(array_size)
                if row[position] == 0:
                    row[position] = 1
                    break
    
    for y_counter, row in enumerate(array):
        for x_counter, cell in enumerate(row):
            background.blit(outer_square, (x_counter * u, y_counter * u))
            if array[y_counter][x_counter] == 1:
                background.blit(black_square, (x_counter * u, y_counter * u))

    screen.blit(background, (0,0))
    screen.blit(square(green), (origin['x']*u, origin['y']*u))
    screen.blit(square(red), (end['x']*u, end['y']*u))

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
