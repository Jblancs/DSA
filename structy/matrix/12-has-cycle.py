# Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. The function should return a boolean indicating whether or not the graph contains a cycle.

# input: adj list of directed graph
# output: boolean indicating whether or not graph contains a cycle
# create cycle_boolean and assign value to False
# for loop to iterate through each point of graph
# create traverse helper function for depth first traversal
# traverse: create visited set to see if cycles to visited node
# traverse: if node in visited reassign cycle_boolean to True
# in for loop if cycle_boolean is true return True
# outside for loop return cycle_boolean

# time O(n) since we traverse through each node

def has_cycle(graph):
  visited = set()
  visiting = set()

  for node in graph:
    if node not in visited:
      result = traverse(node, graph, visiting, visited)
      if result:
        return result
  
  return False

def traverse(node, graph, visiting, visited):
  stack = [node]
  visiting.add(node)

  while stack:
    current = stack.pop()

    if graph[current]:
      for neighbor in graph[current]:
        if neighbor == node:
          return True
        
        if neighbor in visiting:
          return True
        
        if neighbor not in visited: 
          visiting.add(neighbor)
          stack.append(neighbor)

    else:
      visited.update(list(visiting))
      visiting.clear()

  return False

print(has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
})) # -> False

print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
})) # -> True

print(has_cycle({
  "q": ["r", "s"],
  "r": ["t", "u"],
  "s": [],
  "t": [],
  "u": [],
  "v": ["w"],
  "w": [],
  "x": ["w"],
})) # -> False

print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["d"],
  "d": ["b"],
})) # -> True