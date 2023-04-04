import numpy as np


                                                # np.arange

# Create an array of numbers from 0-100 -> 100 is excluded
a = np.arange(100)
print(a)

# Start from 20, end at 100 -> 100 is excluded
a = np.arange(20,100)
print(a)

# Start from 20, end at 100, jump with 3 numbers
a = np.arange(20,100,3)
print(a)


                                                # np.random


# this creates an array of random numbers from 0-10 -> 10 is excluded
b = np.random.permutation(np.arange(10))
print(b)

# creates a random number(int) between 20-30
b = np.random.randint(20,30)
print(b)


# creates a random number between 0-1
b = np.random.rand()
print(b)

# create a 2D array with shape (2, 3) with values from 0-1
b = np.random.rand(2,3)
print(b)
print(b.ndim)  #nr. of dimensions
print(b.shape)

# create a 3D array with shape (2, 3, 4) with values from 0-1
b = np.random.rand(2, 3, 4)
print(b)
print(b.ndim)
print(b.shape)


                                                # np.reshape

# we reshaped the array b above with the shape(2,3,4) into a new shape(2,4,3)
a = b.reshape(2,4,3)
print(a)

# create a 2D numpy array from 0-100 with shape(4,24) -> 4 rows with 25 elements
b = np.arange(100).reshape(4,25)
print(b)
print(b.shape)


# creates a 3D numpy arrays of ones with shape(5,5,5) and dtype int | We give the shape of the array as a tuple
b = np.ones( (5,5,5), dtype = int)
print(b)

# creates a 2D numpy arrays of zeros with shape(5,5) | We give the shape of the array as a tuple
b = np.zeros( (5,5) )
print(b)