import queue
from pathingDisplay import array, origin


class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def neighbors():
    pass


frontier = queue.Queue()
frontier.put(origin)
reached = set()
reached.add(origin)

while not frontier.empty:
    current = frontier.get()