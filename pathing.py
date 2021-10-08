import queue


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

coordinates = tuple[int, int]
def path_finder(start_node: coordinates, end_node: coordinates, array: list[list[int]], navigatable_values: tuple[int] = 0) -> list[coordinates]:
    """A* pathfinding from start_node to end_node in an array.

    Args:
        start_node (tuple of int): starting coordinates.
        end_node (tuple of int): goal coordinates.
        array (list of lists): array to pathfind through
        navigatable_values (tuple of int) : node values in the array that can be navigated.

    Returns:
        list: list of node coordinates from (including) start_node to (including) end_node.
    """
    nodes_to_explore = queue.PriorityQueue()
    origin_node = dict()
    g_cost = dict()  # g cost: # of moves from the start_node
    nodes_to_explore.put((0, start_node))
    origin_node[start_node] = None
    g_cost[start_node] = 0

    while not nodes_to_explore.empty():
        current_node = nodes_to_explore.get()
        if current_node[1] == end_node:
            break
        for new_node in neighbors(current_node[1], array, navigatable_values):
            new_g_cost = g_cost[current_node[1]] + 1
            if new_node not in g_cost or new_g_cost < g_cost[new_node]:
                g_cost[new_node] = new_g_cost
                nodes_to_explore.put((new_g_cost + heuristic_cost(end_node, new_node), new_node))
                origin_node[new_node] = current_node[1]
    
    active_node = end_node
    path = [active_node]
    while active_node != start_node:
        active_node = origin_node[active_node]
        path.append(active_node)
    
    return reversed(path)