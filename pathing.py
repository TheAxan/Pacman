import queue
import pygame
from pathingDisplay import *
import pathingDisplay

start_node = pathingDisplay.origin
end_node = pathingDisplay.end

def neighbors(center_node, array, accepted_neighbor_values):
    neighbors_set = set()
    for i, j in ((-1,0), (0,-1), (1,0), (0,1)):
        try:
            if center_node[0] + i < 0 or center_node[1] + j < 0:
                raise Exception('negative index')
            if array[center_node[1] + j][center_node[0] + i] in accepted_neighbor_values:
                neighbors_set.add((center_node[0] + i, center_node[1] + j))
        except:
            pass
    return neighbors_set

def heuristic_cost(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

nodes_to_explore = queue.PriorityQueue()
origin_node = dict()
g_cost = dict()  # g cost: # of moves from the start_node

nodes_to_explore.put([0, start_node])
origin_node[start_node] = None
g_cost[start_node] = 0

while not nodes_to_explore.empty():
    current_node = nodes_to_explore.get()
    if current_node[1] == end_node:
        break
    for new_node in neighbors(current_node[1], random_array, (0, 3)):
        new_g_cost = g_cost[current_node[1]] + 1
        if new_node not in g_cost or new_g_cost < g_cost[new_node]:
            g_cost[new_node] = new_g_cost
            nodes_to_explore.put([new_g_cost + heuristic_cost(end_node, new_node), new_node])
            origin_node[new_node] = current_node[1]
            screen.blit(orange_square, (new_node[0]*u, new_node[1]*u))

current_node[1] = end_node
while current_node[1] != start_node:
    screen.blit(cyan_square, (current_node[1][0]*u, current_node[1][1]*u))
    current_node[1] = origin_node[current_node[1]]
    pygame.display.flip()
print(input())