import pygame
import pathing
import sys
import copy
import screen as s
from maps import default_map as map_grid



class Entity:
    entities: set[object] =  set()  # to loop through routines
    
    def __init__(self, x: int, y: int, speed_divider: int, original_orientation: str) -> None:
        Entity.entities.add(self)
        
        # self.x is the array x
        self.x: int = x
        self.y: int = y
        
        self.scalar_speed: float = s.cu / speed_divider
        self.orientation_update({
            'up': (0, -1),
            'left': (-1, 0),
            'down': (0, 1),
            'right': (1, 0),
        }[original_orientation])

        self.rect_surface = pygame.Surface((s.cu, s.cu))
        self.rect_surface.set_colorkey(s.black)

        # self.rect.x is the pixel x
        self.rect = self.rect_surface.get_rect()
        self.rect.x = x * s.cu
        self.rect.y = y * s.cu

        self.surface = pygame.transform.scale(self.rect_surface, (s.gu, s.gu))
        self.graphic_rect = self.surface.get_rect()

    def routine(self):
        self.full_cell_check()
        self.rect.move_ip(self.vector_speed)
        self.update_position()
        self.graphic_rect.center = self.rect.center
        s.screen.blit(self.surface, self.graphic_rect)
    
    def full_cell_check(self):
        if self.x == self.rect.x / s.cu and self.y == self.rect.y / s.cu:  # on a full cell
            self.full_cell_routine()
    
    def full_cell_routine(self):
        pass  # defined in subclass

    def tunnel_warp(self):
        if self.y == 14:
            if self.x == -1:
                self.rect.x = 28 * s.cu
            elif self.x == 28:
                self.rect.x = -1 * s.cu
    
    def wall_check(self):
        if (map_grid[self.y + self.orientation[1]]  # cell ahead is a wall
                    [self.x + self.orientation[0]]) == 1:
            self.wall_reaction()

    def wall_reaction():
        pass # defined in subclass

    def update_position(self):
        self.x = round(self.rect.x / s.cu)
        self.y = round(self.rect.y / s.cu)

    def orientation_update(self, new_orientation):
        self.orientation = new_orientation
        self.vector_speed = tuple(self.scalar_speed * x for x in self.orientation)


class Player(Entity):
    def __init__(self, x: int, y: int, speed_divider: int, original_orientation: str, color: tuple[int]) -> None:
        super().__init__(x, y, speed_divider, original_orientation)
        self.input: tuple[int | float] | None = None
        pygame.draw.circle(self.surface, color, (s.gu/2, s.gu/2), s.gu/2)
    
    def input_assignement(self, input):
        self.input = {
            pygame.K_UP: (0, -1),
            pygame.K_LEFT: (-1, 0),
            pygame.K_DOWN: (0, 1),
            pygame.K_RIGHT: (1, 0),
        }[input]
    
    def full_cell_routine(self):
        self.input_handling()
        self.tunnel_warp()
        self.wall_check()
        self.ghost_collision()
    
    def input_handling(self):
        if self.input is not None:
            if not (map_grid[self.y + self.input[1]]  # cell to turn to isn't a wall
                            [self.x + self.input[0]]) == 1:
                if self.x in range(0, 27):
                    self.orientation_update(self.input)
            self.input = None
    
    def wall_reaction(self):
        self.vector_speed = (0, 0)
    
    def ghost_collision(self):
        for entity in Ennemy.ennemies:
            entity.player_collision()
    

class Ennemy(Entity):
    ghost_template = pygame.Surface((s.gu, s.gu))
    pygame.draw.circle(ghost_template, s.white, (s.gu/2, s.gu/2), s.gu/2)
    pygame.draw.rect(ghost_template, s.black, (0, s.gu/2, s.gu, s.gu/2))
    pygame.draw.polygon(ghost_template, s.white, (
        (0, s.gu/2), (0, s.gu), (s.gu/4, s.gu*3/4), (s.gu/2, s.gu), (s.gu*3/4, s.gu*3/4), (s.gu, s.gu), (s.gu, s.gu/2)))

    chase_mode: bool = False
    ennemies: set[object] = set()
    
    def __init__(self, x: int, y: int, speed_divider: int, original_orientation: str, 
                 color: tuple[int], name: str, scatter_target, chase_target) -> None:
        super().__init__(x, y, speed_divider, original_orientation)
        
        self.surface.blit(Ennemy.ghost_template, (0, 0))
        self.surface.fill(color, special_flags=pygame.BLEND_MULT)
        self.name = name
        self.scatter_target = {
            'up-left': (0, 0),
            'up-right': (len(map_grid[0]) - 1, 0),
            'down-left': (0, len(map_grid) -1 ),
            'down-right': (len(map_grid[0]) -1, len(map_grid) -1),
        }.get(scatter_target, 'up-left')
        self.chase_target = {
            'blinky_target': self.blinky_target,
            'pinky_target': self.pinky_target,
            'inky_target': self.inky_target,
            'clyde_target': self.clyde_target,
        }.get(chase_target, 'blinky_targe')


        Ennemy.ennemies.add(self)

    def full_cell_routine(self):
        self.player_collision()
        self.intersection_check()
        self.tunnel_warp()

    def player_collision(self):
        if self.rect.colliderect(pak.rect):
            print(f'Game over, {self.name} got you')  # maybe TODO game over screen
            sys.exit()
    
    def intersection_check(self):
        if map_grid[self.y][self.x] == 2:
            self.next_move_triangulation()
        else:
            self.wall_check()
    
    def next_move_A_star(self):  # maybe TODO A* tunnel consideration
        x, y = pathing.A_star((self.x, self.y), self.target_selection(), self.no_backtrack(map_grid), (1, 3))[1]
        self.orientation = (x - self.x, y - self.y)
        self.vector_speed = tuple(self.scalar_speed * x for x in self.orientation)

    def next_move_triangulation(self):
        x, y = pathing.triangulation((self.x, self.y), self.target_selection(), self.no_backtrack(map_grid), (1, 3))
        self.orientation = (x-self.x, y-self.y)
        self.vector_speed = tuple(self.scalar_speed * x for x in self.orientation)

    def target_selection(self):
        if Ennemy.chase_mode:
            return self.chase_target()
        else:
            return self.scatter_target

    def blinky_target(self):
        return (pak.x, pak.y)

    def pinky_target(self):
        return (pak.x + 4 * pak.orientation[0], pak.y + 4 * pak.orientation[1])

    def inky_target(self):  # a blinky ennemy is required
        return (
            (pak.x + 2 * pak.orientation[0] - blinky.x) * 2 + blinky.x, 
            (pak.y + 2 * pak.orientation[1] - blinky.y) * 2 + blinky.y
        )
    
    def clyde_target(self):
        if ((pak.x - self.x) ** 2 + (pak.y - self.y) ** 2) ** 0.5 <= 8:
            return self.scatter_target
        else:
            return self.blinky_target()
    
    def target_display(self):
        circle_surface = pygame.Surface((s.cu, s.cu))
        circle_surface.set_colorkey(s.black)
        pygame.draw.circle(circle_surface, self.surface.get_at(self.surface.get_rect().center), 
                           (s.cu/2, s.cu/2), s.cu/3)
        if self.chase_target == inky.inky_target:
            s.screen.blit(circle_surface,
                          tuple(i * s.cu for i in (pak.x + 2 * pak.orientation[0], 
                                                   pak.y + 2 * pak.orientation[1])))
        s.screen.blit(circle_surface, tuple(i * s.cu for i in self.target_selection()))

    def no_backtrack(self, array: list[list[int]]):
        temp_array = copy.deepcopy(array)
        temp_array[self.y - self.orientation[1]][self.x - self.orientation[0]] = 1
        return temp_array
        
    def wall_reaction(self):
        if self.orientation[0] == 0:
            if map_grid[self.y][self.x + 1] == 1:
                self.orientation_update((-1, 0))
            else:
                self.orientation_update((1, 0))
        elif self.orientation[1] == 0:
            if map_grid[self.y + 1][self.x] == 1:
                self.orientation_update((0, -1))
            else:
                self.orientation_update((0, 1))

    def turn_around(self):
        self.orientation_update(tuple(-x for x in self.orientation))
            

pak = Player(14, 23, 15, 'left', s.yellow)

blinky = Ennemy(17, 23, 18, 'left', s.red, 'Blinky', 'up-right', 'blinky_target')
inky = Ennemy(22, 14, 18, 'right', s.cyan, 'Inky', 'down-right', 'inky_target')
pinky = Ennemy(16, 29, 18, 'right', s.pink, 'Pinky', 'up-left', 'pinky_target')
clyde = Ennemy(21, 13, 18, 'up', s.orange, 'Clyde', 'down-left', 'clyde_target')
