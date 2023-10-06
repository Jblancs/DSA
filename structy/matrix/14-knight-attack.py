# A knight and a pawn are on a chess board. Can you figure out the minimum number of moves required for the knight to travel to the same position of the pawn? On a single move, the knight can move in an "L" shape; two spaces in any direction, then one space in a perpendicular direction. This means that on a single move, a knight has eight possible positions it can move to.

# Write a function, knight_attack, that takes in 5 arguments:

# n, kr, kc, pr, pc

# n = the length of the chess board
# kr = the starting row of the knight
# kc = the starting column of the knight
# pr = the row of the pawn
# pc = the column of the pawn

# The function should return a number representing the minimum number of moves required for the knight to land ontop of the pawn. The knight cannot move out-of-bounds of the board. You can assume that rows and columns are 0-indexed. This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7. If it is not possible for the knight to attack the pawn, then return None.

# input: length, knight position, pawn position
# output: min moves for knight to land on pawn
# create inbound helper function to confirm if move is inbounds
# create visited set
# create queue for breadth first traversal
# add to queue: tuple of starting r and c and move num 0
# while loop to iterate
# unpack row, col, move from queue.popleft
# create deltas for neighbors of current position
# for loop to iterate through deltas
# if inbounds and not in visited add to visited and queue
# if if neighbor_row and neighbor_col == pr and pc return move + 1
# outside while loop return None

# time: O(n^2) for each space on board
# space: O(n^2) for each position

from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  visited = set()
  queue = deque([(kr,kc,0)])

  while queue:
    row, col, move = queue.popleft()
    deltas = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]

    # get neighbors
    for (r_delta,c_delta) in deltas:
      neighbor_row = row + r_delta
      neighbor_col = col + c_delta

      if neighbor_row == pr and neighbor_col == pc:
        return move + 1

      if inbounds(neighbor_row, neighbor_col, n) and (neighbor_row, neighbor_col) not in visited:
        visited.add((neighbor_row, neighbor_col))
        queue.append((neighbor_row,neighbor_col,move + 1))


  return None

def inbounds(r,c,n):
  r_in = 0 <= r < n
  c_in = 0 <= c < n
  return r_in and c_in

print(knight_attack(8, 1, 1, 2, 2)) # -> 2
print(knight_attack(3, 0, 0, 1, 1)) # -> None
