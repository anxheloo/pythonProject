import numpy as np


# sigmoid function
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])


# output dataset
y = np.array([[0, 0, 1, 1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
weights = 2 * np.random.random((3, 1)) - 1
print(weights)

for iter in range(10000):

    # forward propagation
    inputs = X
    activationFunction = nonlin(np.dot(inputs, weights))
    # print("This is activationFunction", activationFunction)                                                 #6 debug

    # how much did we miss?
    error = y - activationFunction
    # print("This is l1 error", l1_error)                                                                     #7 debug

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = error * nonlin(activationFunction, True)
    # print("This is l1_delta: ", l1_delta)                                                                   #8 debug

    # update weights
    weights += np.dot(inputs.T, l1_delta)
    # print("This is syn0 after update: ", syn0)                                                              #9 debug

print("Output After Training:")

print(activationFunction)