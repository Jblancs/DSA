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
	row = len(mat)
	col = len(mat[0])

	frow = False
	fcol = False

	for idx in range(col):
		if mat[0][idx] == 0:
			frow = True

	for idx in range(row):
		if mat[idx][0] == 0:
			fcol = True

	for i in range(1,row):
		for j in range(1,col):
			if mat[i][j] == 0:
				mat[0][j] = 0
				mat[i][0] = 0

	for i in range(1,row):
		if mat[i][0] == 0:
			for j in range(1,col):
				mat[i][j] = 0

	for i in range(1,col):
		if mat[0][i] == 0:
			for j in range(1,row):
				mat[i][j] = 0

	if fcol:
		for i in range(row):
			mat[i][0] = 0
	if frow:
		for i in range(col):
			mat[0][i] = 0

	return mat
