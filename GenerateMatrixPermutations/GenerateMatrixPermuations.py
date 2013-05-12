"""
GenerateMatrixPermuations.py

This script can be used to generate all the different permuations of a 2x2 matrix
with all values within a range of MIN and MAX

Feburary 2013
Alex Aylwin

"""


#flattenMatrix - not used in this script, but this function
#flattens a matrix into an array
def flattenMatrix(matrix):
	flatArray = []
	size = len(matrix)
	for i in range(len):
		for j in range(len):
			flatArray.append(matrix[i][j])
	return flatArray

#souffleArray - this function 'rises' an array into a square matrix,
#dimensions size x size
def souffleArray(array, size):
	matrix = []
	for i in range(size):
		row = []
		for j in range(size):
			row.append(array[(i*size)+j])
		matrix.append(row)
	return matrix

#fill 4 - this function is the controller function, that creates the
#matricies and calls an operator function on each of them. This other
#function should have side effects that capture the results of whatever
#calculation needs to be performed

#To change the size of the matrix (ie, not 2x2) add for loops to match
#the length of the ARRAY that would come out of flattening the matrix,
#ie a 4x4 matrix should have 16 nested for loops.
def fill4(min, max):
	array = []
	size = 3
	for n1 in range(min, max+1):
		for n2 in range(min, max+1):
			for n3 in range(min, max+1):
				for n4 in range(min, max+1):
					array = [n1,n2,n3,n4]
					matrix = souffleArray(array, size)
					doFunctionOnMatrix(matrix)

#This is the calculation function that actually does some work on the matricies
def doFunctionOnMatrix(matrix):
	print(matrix)

#Kick off the calculation, with a range from 0 - 3, inclusive
fill4(0,3)
