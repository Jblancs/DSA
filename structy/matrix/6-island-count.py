# Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.

# input: grid
# output: number of islands on grid
# create helper function is_inbounds to see if coordinate is inbounds
# create helper function explore for island traversal
# create stack for depth first traversal with initial r,c tuple
# while loop to iterate
# create current by popping off and unpack r,c
# if neighbor is inbounds and value == L
# add to visited
# add to stack

# island_count function
# created visited to hold visited nodes
# create count to hold number of islands
# nested loop for r and c coordinates
# if r,c value == L and not in visited
# add (r,c) to visited
# call explore function
# increment count +1
# return count

# is_inbounds helper function
def is_inbounds(r, c, grid):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])

  return row_inbounds and col_inbounds

# explore helper function
def explore(grid, r, c, visited):
  stack = [(r,c)]

  while stack:
    row, col = stack.pop()

    # top
    if is_inbounds(row-1, col, grid) and (row-1,col) not in visited and grid[row-1][col] == "L":
      visited.add((row-1,col))
      stack.append((row-1,col))

    # right
    if is_inbounds(row, col+1, grid) and (row,col+1) not in visited and grid[row][col+1] == "L":
      visited.add((row,col+1))
      stack.append((row,col+1))

    # bot
    if is_inbounds(row+1, col, grid) and (row+1,col) not in visited and grid[row+1][col] == "L":
      visited.add((row+1,col))
      stack.append((row+1,col))

    # left
    if is_inbounds(row, col-1, grid) and (row,col-1) not in visited and grid[row][col-1] == "L":
      visited.add((row,col-1))
      stack.append((row,col-1))


def island_count(grid):
  count = 0
  visited = set()
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "L" and (r,c) not in visited:
        visited.add((r,c))
        explore(grid, r, c, visited)
        count += 1

  return count

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) # -> 3
