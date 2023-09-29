# Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes.

# input: adj list
# output: length of longest path
# create longest variable to hold longest
# for loop to iterate each point on graph
# create queue
# create length variable starting at 0
# traverse from each starting point
# for loop to add neighbors to queue
# increment length by 1
# outside while loop if length greater than longest reassign
# return longest

from collections import deque

def longest_path(graph):
  distance = {}

  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0

  for node in graph:
    traverse_dist(graph, node, distance)

  return max(distance.values())

def traverse_dist(graph, node, distance):
  stack = [node]
  length = 0

  while stack:
    current = stack.pop()

    if current not in distance:
      distance[current] = length
    else:
      length = distance[current]

    for neighbor in graph[current]:
      distance[neighbor] = length + 1
      stack.append(neighbor)




graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

graph1 = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}



# print(longest_path(graph)) # -> 2
print(longest_path(graph1)) # -> 4
