# Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.

# input: adj list
# output: size of largest component

# helper function to get_comp_size
# traverse using breadth first deque
# create comp_size variable starting at 1
# while loop while queue has value 

from collections import deque

def largest_component(graph):
    pass


largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4
