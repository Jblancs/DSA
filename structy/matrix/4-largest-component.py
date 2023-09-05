# Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.

# input: adj list of undirected graph
# output: size of largest connected component
# create helper breadth_traversal for graph traversal
# create largest_comp to hold number of largest comp
# create visited to hold set of visited nodes
# for loop to iterate each node in graph
# if node not in visited create size variable which calls breadth_traversal to traverse
# if size is greater than largest_comp reassign largest_comp to size
# outside of for loop return largest comp

from collections import deque

# helper function for component size
def get_comp_size(graph, node, visited):
  queue = deque([node])
  comp_size = 1

  while queue:
    current = queue.popleft()
    
    for neighbor in graph[current]:
      if neighbor not in visited:
        queue.append(neighbor)
        visited.add(neighbor)
        comp_size += 1
  
  return comp_size

# iterative solution
# time O(e) for each edge traveled
# space O(n) for stack and set
def largest_component(graph):
  if graph is None:
    return 0
  
  size = 0
  visited = set()

  for node in graph:
    if node not in visited:
      current_size = get_comp_size(graph, node, visited)
      visited.add(node)

      if current_size > size:
        size = current_size

  return size


print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4