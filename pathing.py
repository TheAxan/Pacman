import pygame
import random
import tools
import sys

pygame.init()

u = 30

array_size = 20

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
pygame.draw.rect(outer_square, black, (0, 0, u, u), 1)

while True:
    array = tools.create_empty_array(array_size, array_size)

    origin = {'x': random.randrange(array_size), 'y': random.randrange(array_size)}
    end = {'x': random.randrange(array_size), 'y': random.randrange(array_size)}
    
    for point, value in ((origin, 2), (end, 3)):
        array[point['y']][point['x']] = value
    
    for row in array:
        for _ in range(int(array_size * 0.2)):
            while True:
                position = random.randrange(array_size)
                if row[position] == 0:
                    row[position] = 1
                    break
    
    for y_counter, row in enumerate(array):
        for x_counter, cell in enumerate(row):
            background.blit(outer_square, (x_counter * u, y_counter * u))
            if array[y_counter][x_counter] == 1:
                background.blit(black_square, (x_counter * u, y_counter * u))

    screen.blit(background, (0,0))
    screen.blit(create_square(green, 120), (origin['x']*u, origin['y']*u))
    screen.blit(create_square(red, 120), (end['x']*u, end['y']*u))

    reset_array = False
    while not reset_array:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key is pygame.K_ESCAPE:
                    sys.exit()
                if event.key is pygame.K_BACKSPACE:
                    reset_array = True
            elif event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()
