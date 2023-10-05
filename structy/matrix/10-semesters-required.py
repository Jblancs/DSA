# Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long the prerequisites of a course are satisfied before taking it.

# Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

# You can assume that it is possible to eventually complete all courses.

# create helper function to create graph based on prereqs (adj list)
def create_graph(prereqs):
    graph = {}

    for (a,b) in prereqs:
      if a not in graph:
          graph[a] = []
      if b not in graph:
          graph[b] = []

      graph[b].append(a)

    return graph

# input: num of courses and prereqs
# output: min num of semesters to complete all n courses
# create graph by calling helper function on prereqs
# create sems to hold total number of semester to complete course
# for loop to iterate through graph
# call populate_semester on each node
# return max(sems.values())

# create helper function to populate sems dictionary
def populate_semester(node, graph, sems):
    num_of_sems = 1
    stack = [node]

    while stack:
        current = stack.pop()

        if current not in sems:
            sems[current] = num_of_sems
        else:
            num_of_sems = sems[current]

        for neighbor in graph[current]:
                sems[neighbor] = num_of_sems + 1
                stack.append(neighbor)


# time O(prereqs)
# space O(num_courses) since we store each course in dict

def semesters_required(num_courses, prereqs):
    if len(prereqs) == 0:
        return 1

    graph = create_graph(prereqs)
    sems = {}

    for node in graph:
        if len(graph[node]) == 0:
            sems[node] = 1

    for node in graph:
        populate_semester(node, graph, sems)

    return max(sems.values())


num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
print(semesters_required(num_courses, prereqs)) # -> 3

num_courses = 7
prereqs1 = [
  (4, 3),
  (3, 2),
  (2, 1),
  (1, 0),
  (5, 2),
  (5, 6),
]
print(semesters_required(num_courses, prereqs1)) # -> 5
