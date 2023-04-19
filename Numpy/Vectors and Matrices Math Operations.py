import numpy as np




# For Math Operations both vectors that take place should have the same dimensions

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("v1 vector is: ", v1)
print("v2 vector is: ", v2)

# Gives us a vector that holds the sum of both vectors element-wise on axis = 0
print("v1 + v2 operation is: ", v1 + v2)
print("np.sum function of v1,v2 on axis = 0 is: ", np.sum((v1, v2), axis=0))

# On axis = 1 we get a vector that holds 2 elements: the sum of elements of the v1 and sum of elements of v2
print("np.sum function of v1,v2 on axis = 1 is: ", np.sum((v1, v2), axis=1))

# Gives us a sum of all elements of the vectors.
print("np.sum function by default without specifying any axis is: ", np.sum((v1, v2)))

# Gives us the dot product of 2 vectors: 1*4 + 2*5 + 3*6
v_dot = np.dot(v1, v2)
print("np.dot function of v1 and v2 is: ", v_dot)

# Gives us a third vector of [ v1[0]*v2[0], v1[1]*v2[1], v1[2]*v2[2] ] -> multiply element-wise on axis=0
c = v1 * v2
print("v1 * v2 operations is: ", c)
print("np.multiply function is: ", np.multiply(v1, v2))




# Addition and subtraction: Matrices must have the same dimensions.
# Multiplication: For matrix multiplication, the number of columns in the first matrix must match the number of rows in the second matrix.


A = np.array([[1, 2],
              [3, 4],
              [5, 6]])  # A 3x2 matrix

B = np.array([[7, 8],
              [9, 10]])  # A 2x2 matrix

C = A @ B  # Matrix multiplication
print("A * B product is: ", C)
print("np.matmul function of 2 matrices is: ", np.matmul(A, B))
print("matrix1.dot(matrix2) is : ", A.dot(B))
print(" sum of np.matmul function of both vectors is: ", np.matmul(A, B).sum())



#Matrix and Vector multiplication

a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([2,3,4])

#Multiply a matrix and a vector gives as the a new matrix with same dimensions as given matrix: [ [1*2 + 2*3 + 3*4] ,[4*2 + 5*3 + 6*4] ]
c = a * b
print(c)
                                                        #Both examples are the same
c = np.multiply(a,b)
print(c)

#Dot product: [1*2 + 2*3 + 3*4      4*2 + 5*3 + 6*4 ]
c = a.dot(b)
print(c)