# Write a function def add_arrays(arr1, arr2): that adds two arrays element-wise:
#
# You can assume that arr1 and arr2 are lists of ints/floats
# You must return a new list
# If arr1 and arr2 are not the same shape, return None


import numpy as np

#WAY 1
# def add_arrays(arr1,arr2):
#     if len(arr1) != len(arr2):
#         return None
#
#     result = []
#     for i in range(len(arr1)):
#         sum = arr1[i] + arr2[i]
#         result.append(sum)
#
#     return result

#WAY 2
# def add_arrays(arr1,arr2):
#     if len(arr1) != len(arr2):
#         return None
#     result = []
#     for i in range(len(arr1)):
#         result.append(arr1[i] + arr2[i])
#     return result


#WAY 3 - using numpy
def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None

    x = np.array(arr1)
    y = np.array(arr2)
    c = np.add(x,y)
    return c


arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))