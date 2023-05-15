
#                                                   A[start:end:step]

import numpy as np

# create a numpy array of elements
a = np.arange(100)

# elements of a from 3-50 will be pointed by b
b = a[3:50]
print(b)

# if we change an element of b : it will also update this element in a, cuz it is not a copy but b will point to memory of a
b[0] = -1200
print(a)

# if we dont want this to happen:
b = a[3:10].copy()  # -> this will create a place in memory instead of pointing to a
print(b)


c = a[::5] # is same as c = a[0:100:5]-> from start - end - step is 5

d = a[::-1] #same as : d = np.flip(a) -> reverse the array

e = np.random.rand(2,3)             # -> create a 2d array with dimension 2,3 with random numbers from 0-1
print("our e is : ", e)
e[:,1]                               #-> slice elements of e : get all the rows, and from every row choose the element at column 1
e[1,:]  # same as  e[1][:]           #-> get all columns at row 1
e[0:2,0:2]                           #-> get the rows from 0-2(exclude 2), and columns in each row from 0-2(exclude)

print()

p = np.array([[[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]],

              [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]])


print(p[0:1, :, 1])  #print elements 2,5,8
print(p[1:2, :, 0])  #print elements 1,4,7

print()

l = np.array([1, 2, 3, 4, 5])
print(l[::-1])      #reverse array l

print()



# numpy function to find the index of a given element inside the array
my_array = np.array([1, 2, 3, 4, 5])
index = np.where(my_array == 3)[0]   # -> [0] this gives us only the number we want cuz the print without this will be: (array([2], dtype=int64),)
print(f"The index of our element in the array is: {index}")



# find the index of a given element inside the array
index = 0
for i in my_array:
    if i != 3:
        index+=1
    else:
        print(index)

