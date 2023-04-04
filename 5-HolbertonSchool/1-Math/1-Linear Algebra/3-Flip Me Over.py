# Write a function def matrix_transpose(matrix): that returns the transpose of a 2D matrix, matrix:
#
# You must return a new matrix
# You can assume that matrix is never empty
# You can assume all elements in the same dimension are of the same type/shape

import numpy as np

#WAY 1
def matrix_transpose(matrix):
    transpose = []

    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transpose.append(row)

    return transpose



#WAY 2 - using numpy
def matrix_transpose(matrix):
    transpose = np.array(matrix)

    return transpose.transpose()


mat1 = [[1, 2], [3, 4]]
print(mat1)
print(matrix_transpose(mat1))
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print(mat2)
print(matrix_transpose(mat2))
