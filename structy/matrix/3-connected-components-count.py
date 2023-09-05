# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

# input: adj list of undirected graph
# output: number of connected components within graph
# create helper function depth_traversal to traverse through graph pass in graph, set and node
# create comp_num to count components
# create visited variable to hold set of visited nodes
# for loop to iterate through nodes of graph
# if node not in visited set call depth_traversal func then increment comp_num
# outside for loop return comp_num 

# helper function for graph traversal
def depth_traversal(graph, visited, node):
  stack = [node]

  while stack:
    current = stack.pop()

    for neighbor in graph[current]:
      if neighbor not in visited:
        stack.append(neighbor)
        visited.add(neighbor)

# iterative solution
# time O(e) for each edge travelled
# space O(n) for creating set and stack which would be 2n
def connected_components_count(graph):
  if graph is None:
    return 0

  visited = set()
  comp_num = 0
  
  for node in graph:
    if node not in visited:
      visited.add(node)
      depth_traversal(graph, visited, node)
      comp_num += 1

  return comp_num

print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 2