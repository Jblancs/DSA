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

    # Replace this placeholder return statement with your code
    return []
