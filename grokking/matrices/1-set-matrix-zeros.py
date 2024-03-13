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

def set_matrix_zeros(mat):
	rows = len(mat)
	cols = len(mat[0])
	fcol = False
	frow = False

	for i in range(rows):
		if mat[i][0] == 0:
			fcol = True

	for i in range(cols):
		if mat[0][i] == 0:
			frow = True

	for i in range(1, rows):
		for j in range(1, cols):
			if mat[i][j] == 0:
				mat[0][j] = mat[i][0] = 0

	for i in range(1, rows):
		if mat[i][0] == 0:
			for j in range(1, cols):
				mat[i][j] = 0

	for j in range(1, cols):
		if mat[0][j] == 0:
			for i in range(1, rows):
				mat[i][j] = 0

	if fcol:
		for i in range(rows):
			mat[i][0] = 0

	if frow:
		for j in range(cols):
			mat[0][j] = 0
	return mat
