# Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.

# input: adj list
# output: size of largest component

# helper function to get_comp_size
# traverse using breadth first deque
# create comp_size variable starting at 1
# while loop while queue has value
# create current
# for loop to iterate through neighbors
# if node not in visited
# add node to visited
# add node to queue
# increment comp _size +1
# return comp_size

# create visited set to hold visited nodes
# create largest variable to hold largest comp
# for loop node in graph
# if node not in visited
# add node to visited
# create current and call get_comp_size
# if current > largest reassign to largest to current
# return largest

from collections import deque

def get_comp_size(node, graph, visited):
    queue = deque([node])
    comp_size = 1

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
          if neighbor not in visited:
              visited.add(neighbor)
              queue.append(neighbor)
              comp_size += 1

    return comp_size

def largest_component(graph):
    visited = set()
    largest = 0

    for node in graph:
        if node not in visited:
            visited.add(node)
            current_size = get_comp_size(node, graph, visited)
            if largest < current_size:
                largest = current_size

    return largest


print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4
