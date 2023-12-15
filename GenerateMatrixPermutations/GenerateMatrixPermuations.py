# GenerateMatrixPermutations.py

# souffleArray - this function 'rises' an array into a square matrix,
# dimensions size x size
def souffleArray(array, size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(array[(i * size) + j])
        matrix.append(row)
    return matrix

# fill4 - this function is the controller function, that creates the
# matrices and calls an operator function on each of them. This other
# function should have side effects that capture the results of whatever
# calculation needs to be performed

# To change the size of the matrix (i.e., not 2x2) add for loops to match
# the length of the ARRAY that would come out of flattening the matrix,
# i.e., a 4x4 matrix should have 16 nested for loops.
def fill4(min, max, size, operation_function):
    array = []
    for n1 in range(min, max + 1):
        for n2 in range(min, max + 1):
            for n3 in range(min, max + 1):
                for n4 in range(min, max + 1):
                    array = [n1, n2, n3, n4]
                    matrix = souffleArray(array, size)
                    operation_function(matrix)

# This is the calculation function that actually does some work on the matrices
def doFunctionOnMatrix(matrix):
    print(matrix)
    calculateSum(matrix)
    calculateProduct(matrix)

# Calculate and print the sum of each row and each column in the matrix
def calculateSum(matrix):
    size = len(matrix)
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]

    print(f"Row Sums: {row_sums}")
    print(f"Column Sums: {col_sums}")
    print()

# Calculate and print the product of each row and each column in the matrix
def calculateProduct(matrix):
    size = len(matrix)
    row_products = [1] * size  # Initialize with 1 for each row
    col_products = [1] * size  # Initialize with 1 for each column

    for i in range(size):
        for j in range(size):
            row_products[i] *= matrix[i][j]
            col_products[i] *= matrix[j][i]

    print(f"Row Products: {row_products}")
    print(f"Column Products: {col_products}")
    print()

# Kick off the calculation, with a range from a - b, inclusive, and matrix size 2x2
fill4(1, 6, 2, doFunctionOnMatrix)
