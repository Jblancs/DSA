# Given n×n matrix, rotate the matrix 90 degrees clockwise. The performed rotation should be in place, i.e., the given matrix is modified directly without allocating another matrix.

# input: matrix
# output: matrix rotated 90 degrees clockwise
# init n for length of matrix
# create for loop to iterate row on range n // 2 since we only need to iterate over top half of matrix
# create nested for loop col on range n - row - 1
# swap top left cell with top right
# swap top left with bottom right
# swap top left with bottom left
# return matrix


def rotate_image(matrix):

    n = len(matrix)

    for row in range(n//2):
        for col in range(row, n - row - 1):

            matrix[row][col], matrix[col][n - 1 - row] = matrix[col][n - 1 - row], matrix[row][col]
            matrix[row][col], matrix[n - row - 1][n - col - 1] = matrix[n - row - 1][n - col - 1], matrix[row][col]
            matrix[row][col], matrix[n - col - 1][row] = matrix[n - col - 1][row], matrix[row][col]

    return matrix
