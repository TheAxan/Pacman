import pygame
import pathing
import sys


pygame.display.set_mode()  # The display must be initialized first or it might get the wrong res
u = {  # cells are u lenght squares
    # u must be even or the graphics looks off and wall_stop breaks 
    # because full_cell_check breaks because the resulting speed jumps over full cells.
    # Trying to account for the jump is ressource intensive since the method runs every frame
    (1920, 1080): 34,
    (1080, 1920): 38,
    (2560, 1440): 44,
}.get((pygame.display.Info().current_w, pygame.display.Info().current_h), 30)
screen = pygame.display.set_mode((28 * u, 31 * u), flags=pygame.NOFRAME)

white = 255, 255, 255
black = 0, 0, 0
dark_grey = 15, 15, 15
yellow = 255, 255, 0
blue = 0, 0, 255
red = 255, 0, 0
orange = 255, 153, 0
cyan = 0, 230, 230
pink = 255, 179, 255


default_map = [  # 0 is empty, 1 is a wall, 2 is a turning point
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
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
]  # in python 3.9 my tests showed list access to be much faster than tuple acces, in 3.8 tuples were slightly faster

map_grid = default_map  # this is to have various maps in the future

background = pygame.Surface((28 * u, 31 * u))

square = pygame.Surface((u, u))
square.fill(blue)
pygame.draw.rect(square, dark_grey, (0, 0, u, u), 10)

for y_counter, row in enumerate(map_grid):
    for x_counter, cell in enumerate(row):
        if cell == 1:
            background.blit(square, (x_counter * u, y_counter * u)) # This draws the map


class Entity:
    entities = []  # to loop through routines
    
    def __init__(self, x, y, speed_divider, original_direction) -> None:
        Entity.entities.append(self)
        
        self.surface = pygame.Surface((u, u))
        self.surface.set_colorkey(black)

        # self.rect.x is the pixel x
        self.rect = self.surface.get_rect()
        self.rect.x = x * u
        self.rect.y = y * u

        # self.x is the array x
        self.x = x
        self.y = y
        
        self.speed = u / speed_divider
        self.movement = {
            'left': (-self.speed, 0),
            'up': (0, -self.speed),
            'right': (self.speed, 0),
            'down': (0, self.speed),
        }[original_direction]

    def routine(self):
        self.full_cell_check()
        self.rect.move_ip(self.movement)
        self.update_position()
        screen.blit(self.surface, self.rect)
    
    def update_position(self):
        self.x = round(self.rect.x / u)
        self.y = round(self.rect.y / u)

    def tunnel_warp(self):
        if self.y == 14:
            if self.x == -1:
                self.rect.x = 28 * u
            elif self.x == 28:
                self.rect.x = -1 * u
    
    def full_cell_check(self):
        if self.x == self.rect.x / u and self.y == self.rect.y / u:  # on a full cell
            self.full_cell_routine()

    def full_cell_routine(self):
        pass  # defined in subclass


class Player(Entity):
    def __init__(self, x, y, speed_divider, original_direction, color) -> None:
        super().__init__(x, y, speed_divider, original_direction)
        
        self.input = None
        pygame.draw.circle(self.surface, color, (u/2, u/2), u/2)
    
    def update_direction(self):
        if self.input is not None:
            if not (map_grid[self.y + int(self.input[1] / self.speed)]  # cell to turn to isn't a wall
                            [self.x + int(self.input[0] / self.speed)]) == 1:
                self.movement = self.input
            self.input = None
    
    def wall_stop(self):
        if (map_grid[self.y + int(self.movement[1] / self.speed)]  # cell ahead is a wall
                    [self.x + int(self.movement[0] / self.speed)]) == 1:
            self.movement = (0, 0)
    
    def ghost_collision(self):
        for entity in Entity.entities[1:]:
            entity.player_collision()

    def full_cell_routine(self):
        self.update_direction()
        self.tunnel_warp()
        self.wall_stop()
        self.ghost_collision()
    

class Ennemy(Entity):
    ghost_template = pygame.Surface((u, u))
    pygame.draw.circle(ghost_template, white, (u/2, u/2), u/2)
    pygame.draw.rect(ghost_template, black, (0, u/2, u, u/2))
    pygame.draw.polygon(ghost_template, white, (
        (0, u/2), (0, u), (u/4, u*3/4), (u/2, u), (u*3/4, u*3/4), (u, u), (u, u/2)))

    def __init__(self, x, y, speed_divider, original_direction, color, name) -> None:
        super().__init__(x, y, speed_divider, original_direction)
        
        self.surface.blit(Ennemy.ghost_template, (0, 0))
        self.surface.fill(color, special_flags=pygame.BLEND_MULT)
        self.name = name

    def full_cell_routine(self):
        self.player_collision()
        self.corner_check()
        self.tunnel_warp()

    def corner_check(self):
        if map_grid[self.y][self.x] == 2:
            self.next_move()

    def player_collision(self):
        if self.rect.colliderect(pac.rect):
            print(f'Game over, {self.name} got you')  # maybe TODO game over screen
            sys.exit()
            
    def next_move(self):  # TODO A* pathing target parameters
        path = pathing.path_finder((self.x, self.y), (pac.x, pac.y), map_grid, (0, 2))
        self.movement = ((path[1][0] - path[0][0]) * self.speed, (path[1][1] - path[0][1]) * self.speed)


pac = Player(14, 23, 15, 'left', yellow)
blinky = Ennemy(17, 23, 18, 'left', red, 'Blinky')
inky = Ennemy(22, 14, 18, 'right', cyan, 'Inky')
pinky = Ennemy(16, 29, 18, 'right', pink, 'Pinky')
clyde = Ennemy(21, 13, 18, 'up', orange, 'Clyde')
