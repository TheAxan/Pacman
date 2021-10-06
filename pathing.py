import queue
import pygame
from pathingDisplay import *




def neighbors(center):
    neighbors_list = []
    for i, j in ((-1,0), (0,-1), (1,0), (0,1)):
        try:
            if center[0] + i < 0 or center[1] + j < 0:
                raise Exception('negative index')
            if array[center[1] + j][center[0] + i] == 0 or array[center[1] + j][center[0]] == 3:
                neighbors_list.append((center[0] + i, center[1] + j))
        except:
            pass
    return neighbors_list

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

frontier = queue.PriorityQueue()
frontier.put([0, origin])
came_from = dict()
cost_so_far = dict()
came_from[origin] = None
cost_so_far[origin] = 0

while not frontier.empty():
    current = frontier.get()
    if current[1] == end:
        break
    for next in neighbors(current[1]):
        new_cost = cost_so_far[current[1]] + 1
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            frontier.put([new_cost + heuristic(end, next), next])
            came_from[next] = current[1]
            screen.blit(orange_square, (next[0]*u, next[1]*u))

current[1] = end
while current[1] != origin:
    screen.blit(cyan_square, (current[1][0]*u, current[1][1]*u))
    current[1] = came_from[current[1]]
    pygame.display.flip()
print(input())