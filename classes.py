import pygame

from maps import default_map as map_grid
from initialisation import *


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
    def __init__(self, x, y, speed_divider, original_direction, color, name) -> None:
        super().__init__(x, y, speed_divider, original_direction)
        self.surface.blit(ghost_template, (0, 0))
        self.surface.fill(color, special_flags=pygame.BLEND_MULT)
        self.name = name

    def full_cell_routine(self):
        self.collision()
        self.corner()
        self.tunnel()

    def corner(self):
        if map_grid[self.y][self.x] == 2:
            self.pathing()

    def collision(self):
        if (self.x, self.y) == (pac.x, pac.y):
            print(f'Game over, {self.name} got you')  # TODO game over screen
            exit()
            
    def pathing(self):  # TODO A* pathing
        self.movement = (0, 0)


pac = player(14, 23, 15, 'left', yellow)
blinky = ennemy(17, 23, 18, 'left', red, 'Blinky')
inky = ennemy(22, 14, 18, 'right', cyan, 'Inky')
pinky = ennemy(16, 29, 18, 'right', pink, 'Pinky')
clyde = ennemy(21, 13, 18, 'up', orange, 'Clyde')