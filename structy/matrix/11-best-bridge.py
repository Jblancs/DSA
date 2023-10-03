# Write a function, best_bridge, that takes in a grid as an argument. The grid contains water (W) and land (L). There are exactly two islands in the grid. An island is a vertically or horizontally connected region of land. Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.

# input: grid of island and water
# output: min length bridge between 2 islands
# create visited set for visited nodes
# create explore helper function to traverse an island
# 2 nested loops for find first island then break once island is found
# after loop is broken out of call explore again

# time O(rc) since we have a nested loop
# space O(rc) since we create a queue for breadth first trav

def best_bridge(grid):
  visited = set()
  flag = False
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "L":
        visited.add((r,c))
        explore(visited, grid, "island")
        flag = True
        break

    if flag:
      break

  return explore(visited, grid, "bridge")

# explore helper function
from collections import deque
def explore(visited, grid, type):
  queue = deque([(node, 0) for node in visited])
  
  while queue:
    (r,c),dist = queue.popleft()

    deltas = [(-1,0),(0,1),(1,0),(0,-1)]
    for (delta_r,delta_c) in deltas:
      
      if type == "island" and inbounds(r+delta_r, c+delta_c, grid) and grid[r+delta_r][c+delta_c] == "L" and (r+delta_r,c+delta_c) not in visited:
        visited.add((r+delta_r,c+delta_c))
        queue.append(((r+delta_r, c+delta_c), 0))

      if type == "bridge" and inbounds(r+delta_r, c+delta_c, grid) and (r+delta_r,c+delta_c) not in visited:
        if grid[r+delta_r][c+delta_c] == "L":
          return dist
        else:
          visited.add((r+delta_r, c+delta_c))
          queue.append(((r+delta_r, c+delta_c),dist+1))
    

# create inbounds helper function
def inbounds(r,c,grid):
  r_in = 0 <= r < len(grid)
  c_in = 0 <= c < len(grid[0])

  return r_in and c_in
  
   

grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
print(best_bridge(grid)) # -> 1