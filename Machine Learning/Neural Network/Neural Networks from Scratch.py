import numpy as np

'''
1- We build a simple network with 3 inputs, 3 weights, 1 bias and  1 output. 
    
inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2 -> nr of biases = number of neurons in hidden layers & output neurons ( exclude the neuron on the input layers)
            In our case we have 3 inputs and 1 output so we have 1 bias for the output neuron.

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)
'''


'''
2- Lets model a simple network with 4 inputs & 3 outputs.
    What is going to change is the number of weight sets & nr. of biases. For every unique output neturon we got a unique set of weights
    Nr. of weight sets is equal to the number of the corresponding output neurons for that layer. 
    3 output neurons -> 3 weights sets
    3 output neurons -> 3 biases
    
 
inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [
          inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3
          ]


'''

'''
3-Lets simplify the code above, instead of manually typing output results, we use the for loop.

output = [] # Output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    output.append(neuron_output)

print(output)
'''



'''
4-Dot Product of 2 Vectors:

inputs = [1, 2, 3, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2

The operations of this is : 
    inputs[0] * weights[0] + 
    inputs[1] * weights[1] + 
    inputs[2] * weights[2] + 
    inputs[3] * weights[3] + 
    bias
 
output = np.dot(weights, inputs) + bias

print(output)
'''

'''
5-The Dot Product of a Matrix of Vectors and 1 Vector:

inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases 
Note : np.dot(weights, inputs) = [np.dot(weights[0], inputs), np.dot(weights[1], inputs), np.dot(weights[2], inputs)]
       The reason we put 'weights' first in np.dot is: because 'shape of weights matrix is: (3,4)', 'shape of inputs vector is: (4,)'.
       So to multiply 2 matrixes or matrix and a vector we need to have nr.of columns of the 1 matrix must equal the nr. of rows of 2 matrix.
       In our case: 'shape of weights matrix is: (3,4)', 'shape of inputs vector is: (4,)', our output will be a vector with shape (3,).

print(output)
'''



'''
6-Batches,Layers and Objects

import numpy as np

# The inputs now are a batch of inputs
inputs = [
    [1, 2, 3, 2.5],
    [2.0,5.0,-1.0,2.0],
    [-1.5,2.7,3.3,-0.8]
]

weights = [[0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

# Layer 2
weights2 = [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]]

biases2 = [-1, 2, -0.5]


#Note: In order to perform 2 matrixes multiplication we need to have the nr. of columns(n=4)of 'inputs' with shape (3,4) equal to the number of rows of 'weights' matrix with shape (3,4)
    #Thas why we use the trasnpose function of numpy to turn the weights matrix(n,p) to a new shape of (4,3).
    # And now we have nr of culumns of 'inputs' : (m,n) -> 'n' = 4 equal to nr of rows of 'weights' : (n,p) -> 'n=4'
layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
print(layer1_outputs)

layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2
print(layer2_outputs)

'''


'''
7-Using OOP

import numpy as np

np.random.seed(0)

X = [[1, 2, 3, 2.5],
    [2.0,5.0,-1.0,2.0],
    [-1.5,2.7,3.3,-0.8]]

class Layer_Dense:
    def __init__(self,n_inputs, n_neurons):
        #Note: Previous when we created weights, we created the shape based on the : (nr.of neurons outputed, inputs)
        #Now in order to eleminate that transpose function everytime we need to make this calculations we build this way.
        self.weights = 0.10*np.random.randn(n_inputs ,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)
'''