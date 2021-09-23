import pygame
import sys
from math import floor, ceil

pygame.init()

# general definitions
map_grid = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1),
    (0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1),
    (0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1),
    (1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1),
    (1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
    (1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)

u = 38      # 1 unit is 30 pixels by default (840x930), 38 for 1064x1178, 34 for 952x1054
screen = pygame.display.set_mode((28 * u, 31 * u))

# colors definition
white = 255, 255, 255
black = 0, 0, 0
dark_grey = 15, 15, 15
yellow = 255, 255, 0
blue = 0, 0, 255

# background surface
background = pygame.Surface((28 * u, 31 * u))

square = pygame.Surface((u, u))     # Each cell is a squares of 1 unit
square.fill(blue)
pygame.draw.rect(square, dark_grey, (0, 0, u, u), 10)       # This is to identify separate squares visually

y_counter = 0
for row in map_grid:
    x_counter = 0
    for i in row:
        if i:
            background.blit(square, (x_counter * u, y_counter * u))     # This draws the map
        x_counter += 1
    y_counter += 1


class entity:
    def __init__(self, x, y, speed_divider, direction) -> None:
        self.surface = pygame.Surface((u, u))
        self.surface.set_colorkey(black)
        self.rect = self.surface.get_rect()
        self.rect.x = x * u
        self.rect.y = y * u
        self.x = x
        self.y = y
        self.speed = u / speed_divider
        self.movement = {
            'left': (-self.speed, 0),
            'up': (0, -self.speed),
            'right': (self.speed, 0),
            'down': (0, self.speed),
        }[direction]

pac = entity(14, 23, 15, 'left')
pygame.draw.circle(pac.surface, yellow, (u/2, u/2), u/2)

# Program definitions
direction_input = None
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_LEFT, pygame.K_UP,
                                                          pygame.K_RIGHT, pygame.K_DOWN):
            direction_input = {
                
                # Probably want to reorganize this
                
                pygame.K_LEFT: (-pac.speed, 0),
                pygame.K_UP: (0, -pac.speed),
                pygame.K_RIGHT: (pac.speed, 0),
                pygame.K_DOWN: (0, pac.speed),
            }[event.key]
        elif event.type == pygame.QUIT:
            sys.exit()

    # change movement to direction input on full squares
    if direction_input is not None and pac.x == pac.rect.x / u and pac.y == pac.rect.y / u:
        if (map_grid[int(pac.y + direction_input[1] / pac.speed)]
                    [int(pac.x + direction_input[0] / pac.speed)]) == 0:
            pac.movement = direction_input
            direction_input = None
        else:
            direction_input = None

    # Move pac before cell update and wall-check to prevent wall ramming
    pac.rect.move_ip(pac.movement)

    # Update cell position
    if pac.movement[0] == -pac.speed:
        pac.x = floor(pac.rect.x / u)
    elif pac.movement[0] == pac.speed:
        pac.x = ceil(pac.rect.x / u)

    elif pac.movement[1] == -pac.speed:
        pac.y = floor(pac.rect.y / u)
    elif pac.movement[1] == pac.speed:
        pac.y = ceil(pac.rect.y / u)

    # Immobilizes and resets pos if cell ahead is a wall
    if map_grid[pac.y][pac.x]:
        pac.movement = (0, 0)
        pac.rect.x = round(pac.rect.x / u) * u
        pac.rect.y = round(pac.rect.y / u) * u
        pac.x = int(pac.rect.x / u)
        pac.y = int(pac.rect.y / u)

    # Tunnel
    if pac.y == 14:
        if pac.x == -2:
            pac.rect.x = 29 * u
        elif pac.x == 29:
            pac.rect.x = -2 * u

    # Refresh screen
    screen.blit(background, (0, 0))
    screen.blit(pac.surface, pac.rect)

    clock.tick(60)
    pygame.display.flip()
