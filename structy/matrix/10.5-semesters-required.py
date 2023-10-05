# Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long the prerequisites of a course are satisfied before taking it.

# Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

# You can assume that it is possible to eventually complete all courses.

# create adj_list helper to create graph
def adj_list(prereqs):
  graph = {}
  for (a, b) in prereqs:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[b].append(a)

  return graph

# create update_semesters helper function
def update_semesters(graph, node, semesters):
  sems = 1
  stack = [node]

  while stack:
    current = stack.pop()

    if current not in semesters:
      semesters[current] = sems
    else:
      sems = semesters[current]

    for neighbor in graph[current]:
      semesters[neighbor] = sems + 1
      stack.append(neighbor)


# input: num of courses (n) and list of prereqs
# output: min number of semesters to complete all n courses
# create graph using adj_list helper
# create semesters dict to hold num of semesters for each class
# for loop to iterate through graph and call helper update_semseters
# return max of semesters.values()

def semesters_required(num_courses, prereqs):
  if prereqs is None:
    return 1

  graph = adj_list(prereqs)
  semesters = {}

  for node in graph:
    if len(graph[node]) == 0:
      semesters[node] = 1

  for node in graph:
    update_semesters(graph, node, semesters)

  return max(semesters.values())


num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
print(semesters_required(num_courses, prereqs)) # -> 3
