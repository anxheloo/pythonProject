
import numpy as np


v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v_sum = v1 + v2
print(v_sum)
print(np.sum((v1,v2),axis=0))


v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v_dot = np.dot(v1, v2)
print(v_dot)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b
print(c)
print(np.multiply(a,b))
print(np.dot(a,b))




A = np.array([[1, 2],
              [3, 4],
              [5, 6]])  # A 3x2 matrix

B = np.array([[7, 8],
              [9, 10]])  # A 2x2 matrix


C = A @ B  # Matrix multiplication
print(C)
print(np.matmul(A,B))
print(A.dot(B))
print(np.matmul(A,B).sum())
