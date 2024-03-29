# input: n for number of ball and grid
# output: array size n with ith element indiccating column that ball falls out of or -1 if stuck

# init rows to len(grid)
# init cols to len(grid[0])
# init result array
# iterate grid using nested loops
# For each row, compute next column by adding current_col to grid[row][current_col]
# check if grid[row][next_col] has same val as grid[row][current_col] ball can move
# check if ball is not stuck at boundary by checking if next_col is < 0 or > than cols
# set current_col as next_col


def find_exit_column(grid):

    rows = len(grid)
    cols = len(grid[0])
    result = []

    for col in range(cols):
        current_col = col
        for row in range(rows):
            next_col = current_col + grid[row][current_col]

            if next_col < 0 or next_col > cols-1 or grid[row][current_col] != grid[row][next_col]:
                result.append(-1)
                break

            if row == rows - 1:
                result.append(next_col)


            current_col = next_col

    return result
