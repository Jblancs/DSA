# Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses.

# input: number of courses and prereqs
# output: boolean indicating if possible to complete all courses
# create graph helper function to create adj_list
# create visited set
# create visiting set
# for loop to iterate through graph
# if result is False return False
# outside loop return True
# create traverse helper function
# create stack for depth first traversal
# while loop to traverse
# create current by popping off stack
# for loop to iterate through neighbors
# if neighbor in visiting return False
# if neighbor == node return False
# if neighbor not in visited add to visited and stack
# visited.update with visiting values
# clear visiting

# time O(n + p) num of courses and prereqs
# space O(n + p) num of courses and prereqs

def prereqs_possible(num_courses, prereqs):
  visited = set()
  visiting = set()
  graph = create_graph(prereqs)
  print(graph)

  for node in graph:
    if node not in visited:
      result = traverse(node, graph, visited, visiting)
      if result:
        return False

  return True

def traverse(node, graph, visited, visiting):
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

    visited.update(list(visiting))
    visiting.clear()

  return False


def create_graph(prereqs):
  graph = {}

  for (a,b) in prereqs:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[b].append(a)

  return graph

numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
print(prereqs_possible(numCourses, prereqs)) # -> True

numCourses = 6
prereqs1 = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
  (3, 0),
]
print(prereqs_possible(numCourses, prereqs1)) # -> False

numCourses = 5
prereqs2 = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
]
print(prereqs_possible(numCourses, prereqs2)) # -> True
