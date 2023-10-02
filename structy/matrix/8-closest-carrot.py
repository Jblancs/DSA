# Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number representing the length of the shortest path from the starting position to a carrot. You may move up, down, left, or right, but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.

# input: grid, starting r and c
# output: distance to closes carrot
# create queue using deque for breadth first traversal
# in queue enter a tuple containing starting row, col and distance (starting at 0)
# create visited set to hold visited nodes
# while queue has value, iterate through nodes
# unpack r,c,dist using popleft()
# if neighbor is inbounds and not "X" and not in visited
# if neight is "C" return dist + 1
# add tuple to set
# add tuple to queue and increment dist + 1
# outside loop return -1

# create is_inbounds helper function
def is_inbounds(r,c,grid):
  row_in = 0 <= r < len(grid)
  col_in = 0 <= c < len(grid[0])
  return row_in and col_in

#iterative solution
# time O(rc) since we traverse through graph
# space O(rc) for set and queue

from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  queue = deque([(starting_row, starting_col, 0)])
  visited = set()

  while queue:
    (r, c, dist) = queue.popleft()

    # get neighbors
    delta = [(-1,0),(0,1),(1,0),(0,-1)]

    for (delta_row, delta_col) in delta:
      if is_inbounds(r+delta_row,c+delta_col,grid) and grid[r+delta_row][c+delta_col] != "X" and (r+delta_row,c+delta_col) not in visited:

        visited.add((r+delta_row,c+delta_col))

        if grid[r+delta_row][c+delta_col] == "C":
          return dist + 1
        queue.append((r+delta_row,c+delta_col,dist+1))

  return -1

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2)) # -> 4
