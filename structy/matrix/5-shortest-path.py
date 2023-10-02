# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.

def create_adj_list(edges):
  adj_list = dict()

  for (first, second) in edges:
    if first not in adj_list:
      adj_list[first] = []

    if second not in adj_list:
      adj_list[second] = []

    adj_list[first].append(second)
    adj_list[second].append(first)

  return adj_list

# input: edges and 2 nodes
# output shortest distance between 2 nodes
# create adj list helper function
# create queue breadth first traversal for efficiency (depth would travel too much if wrong path chosen)
# should insert tuple containing node and distance
# create set for visited nodes
# unpack tuple node, distance using popleft
# for loop to iterate through nodes neighbors
# if neighbor is not in visited
# add to visited
# if neighbor == node_B return distance + 1
# else append tuple (neighbor, distance + 1) to queue
# outside of loop return -1

# time O(n) because we traverse through each node
# space O(n) because we create set and queue

from collections import deque

def shortest_path(edges, node_A, node_B):
  queue = deque([(node_A, 0)])
  visited = set([node_A])
  graph = create_adj_list(edges)

  while queue:
    node, distance = queue.popleft()

    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)

        if neighbor == node_B:
          return distance + 1
        else:
          queue.append((neighbor, distance+1))

  return -1


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z')) # -> 2
