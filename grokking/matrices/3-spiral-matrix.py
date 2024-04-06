# Given an m×n matrix, return an array containing the matrix elements in spiral order, starting from the top-left cell.

# input: matrix
# output: array with values in spiral order
# init rows to length of matrix
# init cols to length of matrix row
# init row to 0 and col to -1
# init direction to 1 if moving right/up and -1 if moving down/left
# init result to empty array
# while loop to iterate while rows and cols > 0
# for loop to iterate cols
# add direction to col
# append current val to result
# outside loop rows -= 1 since we do not want to repeat a row
# for loop to iterate rows
# add direction to row
# append val to result
# outside loop cols -= 1 so we don't repeat
# direction *= -1 to reverse direction
# return result


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
