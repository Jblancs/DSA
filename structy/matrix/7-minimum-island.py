# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.

# create is_inbounds helper function to ensure neighbor is in bounds
def is_inbounds(r,c,grid):
  row_in = 0 <= r < len(grid)
  col_in = 0 <= c < len(grid[0])
  return row_in and col_in

# create island_size helper to calculate size of island
def get_island_size(r,c,grid,visited):
  stack = [(r,c)]
  size = 1

  while stack:
    row, col = stack.pop()

    # top
    if is_inbounds(row-1,col,grid) and (row-1,col) not in visited and grid[row-1][col] == "L":
      visited.add((row-1,col))
      stack.append((row-1,col))
      size += 1

    # right
    if is_inbounds(row,col+1,grid) and (row,col+1) not in visited and grid[row][col+1] == "L":
      visited.add((row,col+1))
      stack.append((row,col+1))
      size += 1

    # bot
    if is_inbounds(row+1,col,grid) and (row+1,col) not in visited and grid[row+1][col] == "L":
      visited.add((row+1,col))
      stack.append((row+1,col))
      size += 1

    # left
    if is_inbounds(row,col-1,grid) and (row,col-1) not in visited and grid[row][col-1] == "L":
      visited.add((row,col-1))
      stack.append((row,col-1))
      size += 1

  return size

# input: grid
# output: size of smallest island
# create smallest variable to hold island and assign it to infinity
# create visited set to track visited nodes
# nested loop for r and c coordinates
# if (r,c) is not in visited and grid[r][c] == L
# create island_size variable and assign it to the value of get_island_size
# compare island_size to smallest island and reassign smallest island to island_size if smaller
# return smallest_island

# time O(rc) because we traverse through grid to find smallest island
# space O(rc) because we create a set and stack

def minimum_island(grid):
  smallest_island = float('inf')
  visited = set()

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "L" and (r,c) not in visited:
        visited.add((r,c))
        island_size = get_island_size(r,c,grid,visited)
        if island_size < smallest_island:
          smallest_island = island_size

  return smallest_island

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid)) # -> 2
