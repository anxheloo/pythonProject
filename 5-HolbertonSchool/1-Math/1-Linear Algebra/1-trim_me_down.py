# Complete the following source code (found below):
#
# the_middle should be a 2D matrix containing the 3rd and 4th columns of matrix
# You are not allowed to use any conditional statements
# You are only allowed to use one for loop
# Your program should be exactly 6 lines


#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]

#WAY 1
the_middle = []
the_middle.append(matrix[0][2:4])
the_middle.append(matrix[1][2:4])
the_middle.append(matrix[2][2:4])

#WAY 2
# for i in range(len(matrix)):
#     the_middle.append(matrix[i][2:4])

print("The middle columns of the matrix are: {}".format(the_middle))