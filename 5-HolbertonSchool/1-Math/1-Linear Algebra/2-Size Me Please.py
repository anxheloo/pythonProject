# Write a function def matrix_shape(matrix): that calculates the shape of a matrix:
#
# You can assume all elements in the same dimension are of the same type/shape
# The shape should be returned as a list of integers

import numpy as np


#WAY 1
def matrix_shape(matrix):
    result = []
    result.append(len(matrix))

    for i in range(len(matrix)-1):
        result.append(len(matrix[i]))
        if isinstance(matrix[i][i], list):
            result.append(len(matrix[i][i]))

    return result



#WAY 2
# def matrix_shape(matrix):
#
#     result = []
#
#     while(type(matrix) is list):
#         result.append(len(matrix))
#         matrix = matrix[0]
#     return result


#WAY 3 - Using numpy
# def matrix_shape(matrix):
#     shapeWeWant = np.array(matrix)
#     return shapeWeWant.shape

mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))
mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print(matrix_shape(mat2))