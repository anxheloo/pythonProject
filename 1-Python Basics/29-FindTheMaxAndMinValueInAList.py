import math

mat1 = [1, 2, 3, 4]


#WAY1
# min = 200000000000000000
# max = 0
# for i in range(len(mat1)):
#     if(mat1[i] > max):
#         max = mat1[i]
#
#     if(min > mat1[i]):
#         min = mat1[i]



#WAY 2
# mat = [8,7, 1, 2, 3, 4]
# min = mat[0]
# max = mat[0]
#
# for i in range(len(mat)):
#     if(mat[i] > max):
#         max = mat[i]
#
#     if(min > mat[i]):
#         min = mat[i]
#
# print("The maximum is : " + str(max))
# print("The maximum is : " + str(min))
#




#WAY 3 - Using math functions
numbers = [5, 2, 9, 1, 7, 4]

# find the maximum number in the list
max_number = max(numbers)
print("Maximum number:", max_number)

# find the minimum number in the list
min_number = min(numbers)
print("Minimum number:", min_number)
