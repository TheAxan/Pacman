import pygame
from sys import exit

pygame.init()

# general definitions
map_grid = [  # 0 is empty, 1 is a wall, 2 is a turning point
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 2, 0, 0, 0, 0, 2, 1, 1, 2, 0, 0, 2, 1, 1, 2, 0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 2, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 0],
    [0, 2, 2, 2, 2, 1, 0, 1, 1, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 1, 1, 0, 1, 2, 2, 2, 2, 0],
    [0, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 0],
    [0, 2, 2, 2, 2, 1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 1, 2, 2, 2, 2, 0],
    [0, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 1, 1, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 2, 0, 2, 1, 1, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 1, 1, 2, 0, 2, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 2, 0, 2, 0, 0, 2, 1, 1, 2, 0, 0, 2, 1, 1, 2, 0, 0, 2, 1, 1, 2, 0, 0, 2, 0, 2, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


clock = pygame.time.Clock()

pygame.display.set_mode()  # The display must be initialized first or it might get the wrong res
u = {  # 1 unit is 30 pixels by default (840x930), 38 for 1064x1178, 34 for 952x1054
    (1920, 1080): 34,
    (1080, 1920): 38,
}.get((pygame.display.Info().current_w, pygame.display.Info().current_h), 30)
screen = pygame.display.set_mode((28 * u, 31 * u))

# colors definition
white = 255, 255, 255
black = 0, 0, 0
dark_grey = 15, 15, 15
yellow = 255, 255, 0
blue = 0, 0, 255
red = 255, 0, 0
orange = 255, 153, 0
cyan = 0, 230, 230
pink = 255, 179, 255

# background surface
background = pygame.Surface((28 * u, 31 * u))

square = pygame.Surface((u, u)) # Each cell is a squares of 1 unit
square.fill(blue)
pygame.draw.rect(square, dark_grey, (0, 0, u, u), 10)  # This is to identify separate squares visually

y_counter = 0
for row in map_grid:
    x_counter = 0
    for cell in row:
        if cell == 1:
            background.blit(square, (x_counter * u, y_counter * u)) # This draws the map
        x_counter += 1
    y_counter += 1

entities = []

class entity:
    def __init__(self, x, y, speed_divider, original_direction) -> None:
        entities.append(self)
        
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
        }[original_direction]

    def update_pos(self):
        self.x = round(self.rect.x / u)
        self.y = round(self.rect.y / u)

    def tunnel(self):
        if self.y == 14:
            if self.x == -1:
                self.rect.x = 28 * u
            elif self.x == 28:
                self.rect.x = -1 * u
    
    def full_cell(self):  # Check if the object is on a full cell
        if self.x == self.rect.x / u and self.y == self.rect.y / u:
            self.full_cell_routine()

    def full_cell_routine(self):
        pass  # defined in subclass

    def routine(self):
        self.full_cell()
        self.rect.move_ip(self.movement)
        self.update_pos()
        screen.blit(self.surface, self.rect)
    

class player(entity):
    def __init__(self, x, y, speed_divider, original_direction, color) -> None:
        super().__init__(x, y, speed_divider, original_direction)
        self.input = None
        pygame.draw.circle(self.surface, color, (u/2, u/2), u/2)
    
    def update_direction(self):
        if self.input is not None:    
            if not (map_grid[self.y + int(self.input[1] / self.speed)]
                            [self.x + int(self.input[0] / self.speed)]):
                self.movement = self.input
            self.input = None
    
    def wall_stop(self):
        if (map_grid[self.y + int(self.movement[1] / self.speed)]
                    [self.x + int(self.movement[0] / self.speed)]) == 1:
            self.movement = (0, 0)
    
    def full_cell_routine(self):
        self.update_direction()
        self.tunnel()
        self.wall_stop()
    

ghost_template = pygame.Surface((u, u))
pygame.draw.circle(ghost_template, white, (u/2, u/2), u/2)
pygame.draw.rect(ghost_template, black, (0, u/2, u, u/2))
pygame.draw.polygon(ghost_template, white, ((0, u/2), 
                                            (0, u), 
                                            (u/4, u * 3/4), 
                                            (u/2, u), 
                                            (u * 3/4, u * 3/4), 
                                            (u, u), 
                                            (u, u/2)))


class ennemy(entity):
    def __init__(self, x, y, speed_divider, original_direction, color) -> None:
        super().__init__(x, y, speed_divider, original_direction)
        self.surface.blit(ghost_template, (0, 0))
        self.surface.fill(color, special_flags=pygame.BLEND_MULT)
    
    def full_cell_routine(self):
        self.corner()
        self.tunnel()

    def corner(self):
        if map_grid[self.y][self.x] == 2:
            self.pathing()

    def pathing(self):  # todo A* pathing
        self.movement = (0, 0)


pac = player(14, 23, 15, 'left', yellow)


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN):
                pac.input = {
                    pygame.K_LEFT: (-pac.speed, 0),
                    pygame.K_UP: (0, -pac.speed),
                    pygame.K_RIGHT: (pac.speed, 0),
                    pygame.K_DOWN: (0, pac.speed),
                }[event.key]
            elif event.key is pygame.K_ESCAPE:
                exit()
            elif event.key in ():
                pass
        
        elif event.type == pygame.QUIT:
            exit()


    screen.blit(background, (0, 0))  # reset background
    for entity in entities:
        entity.routine()

    clock.tick(60)
    pygame.display.flip()
