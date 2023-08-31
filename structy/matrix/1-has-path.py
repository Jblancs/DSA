# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

# Hey. This is our first graph problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

# input: adj list and 2 nodes
# output: boolean if path between src node and dst node
# create queue for a depth first trav starting with src
# while queue has node iterate
# create current by popleft
# if current == dst return true
# for loop to iterate and append neighbors
# outside loop return false

# acyclic mean no cycle

from collections import deque

# time: O(e) which is number of edges since we need to traverse through each edge
# space: O(n) since we are added every node to queue
def has_path(graph, src, dst):
  queue = deque([src])

  while queue:
    current = queue.popleft()

    if current == dst:
      return True

    for node in graph[current]:
      queue.append(node)

  return False

# recursive solution
def has_path_recur(graph, src, dst):
  if src == dst:
    return True

  for node in graph[src]:
    if has_path_recur(graph, node, dst) == True:
      return True

  return False




graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k')) # True
print(has_path_recur(graph, 'f', 'k')) # True
