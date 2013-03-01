def flattenMatrix(matrix):
	flatArray = []
	size = len(matrix)
	for i in range(len):
		for j in range(len):
			flatArray.append(matrix[i][j])
	return flatArray

def souffleArray(array, size):
	matrix = []
	for i in range(size):
		row = []
		for j in range(size):
			row.append(array[(i*size)+j])
		matrix.append(row)
	return matrix

def fill4(min, max):
	array = []
	size = 2
	for n1 in range(min, max+1):
		for n2 in range(min, max+1):
			for n3 in range(min, max+1):
				for n4 in range(min, max+1):
					array = [n1,n2,n3,n4]
					matrix = souffleArray(array, size)
					doFunctionOnMatrix(matrix)

def doFunctionOnMatrix(matrix):
	print(matrix)


fill4(0,3)
