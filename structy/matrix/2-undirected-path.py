# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

# input: list of edges, node a, node b
# output: boolean if path exists from a to b
# convert list of edges to adj list using a for loop
# create a set to record nodes already traveled to
# create queue for depth first traversal
# while loop to iterate while queue has value
# create current with popleft
# if current == node_b return True
# for loop to iterate neighbors
# in loop check set if neighbor not included in set append and add to set
# outside both loops return False

from collections import deque

# helper to convert edges to adj_list
def build_graph(edges):
  adj_list = {}

  for (node_1, node_2) in edges:
    if node_1 not in adj_list:
      adj_list[node_1] = []

    if node_2 not in adj_list:
      adj_list[node_2] = []

    adj_list[node_1].append(node_2)
    adj_list[node_2].append(node_1)

  return adj_list

# iterative solution
def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)

  # set needed to avoid inf loop
  visited_nodes = set(node_A)
  queue = deque([node_A])
  while queue:
    current = queue.popleft()

    if current == node_B:
      return True

    for neighbor in graph[current]:
      if neighbor not in visited_nodes:
        queue.append(neighbor)
      visited_nodes.add(neighbor)

  return False


# recursive solution
def undirected_path_recur(edges, node_A, node_B):
  graph = build_graph(edges)
  return has_path(graph, node_A, node_B, set())

def has_path(graph, src, dst, visited):
  if src == dst:
    return True

  if src in visited:
    return False

  visited.add(src)

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) is True:
      return True

  return False

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'j', 'm')) # -> True
print(undirected_path_recur(edges, 'j', 'm')) # -> True
