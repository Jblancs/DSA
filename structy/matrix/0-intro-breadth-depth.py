graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

# Depth first traversal
def depth_first_print(graph, start):
    stack = [start]

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

# Depth first recursive
def depth_first_print_recur(graph, current):
    print(current)

    for neighbor in graph[current]:
        depth_first_print_recur(graph, neighbor)

depth_first_print(graph, "a")
depth_first_print_recur(graph, "a")

# Breadth first traversal
# always done iteratively since recursion uses a stack

from collections import deque

def breadth_first_print(graph, start):
    queue = deque([start])

    while len(queue) > 0:
        current = queue[0]
        print(current)
        queue.popleft()

        for neighbor in graph[current]:
            queue.append(neighbor)

breadth_first_print(graph, "a")
