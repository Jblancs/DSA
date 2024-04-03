# input: matrix
# output: matrix with row/col containing 0 set to 0
# init rows and cols number of rows/cols in matrix
# init fcol and frow to false
# iterate through first row and set frow to true if there is a 0
# do the same with fcol
# iterate over matrix and if 0 is found set first element in row and col to 0
# iterate over first element in each row and if 0 set whole ROW to 0s
# iterate over first element in each col and if 0 set whole COL to 0s
# if fcol or frow true set respective 0

# time: O(m x n)
# space: O(1)

def set_matrix_zeros(mat):
	rows = len(mat)
	cols = len(mat[0])

	frow = False
	fcol = False

	for idx in range(rows):
		if mat[idx][0] == 0:
			fcol = True

	for idx in range(cols):
		if mat[0][idx] == 0:
			frow = True

	for row in range(1,rows):
		for col in range(1,cols):
			if mat[row][col] == 0:
				mat[0][col] = 0
				mat[row][0] = 0

	for row_idx in range(1,rows):
		if mat[row_idx][0] == 0:
			for col_idx in range(1,cols):
				mat[row_idx][col_idx] = 0

	for col_idx in range(1,cols):
		if mat[0][col_idx] == 0:
			for row_idx in range(1,rows):
				mat[row_idx][col_idx] = 0


	if frow:
		for col_idx in range(cols):
			mat[0][col_idx] = 0

	if fcol:
		for row_idx in range(rows):
			mat[row_idx][0] = 0

	return mat
