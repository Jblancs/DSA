# Given an m×n matrix, return an array containing the matrix elements in spiral order, starting from the top-left cell.

# input: matrix
# output: array with values in spiral order

def spiral_order(matrix):

  rows, cols = len(matrix), len(matrix[0])
  row, col = 0, -1
  direction = 1
  result = []

  while rows > 0 and cols > 0:
    for _ in range(cols):
      col += direction
      result.append(matrix[row][col])

    rows -= 1

    for _ in range(rows):
      row += direction
      result.append(matrix[row][col])

    cols -= 1
    direction *= -1

  return result
