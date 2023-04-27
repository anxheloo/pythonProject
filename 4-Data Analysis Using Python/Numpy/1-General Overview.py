import numpy as np

#If we dont specify the data type, it is by default specified based on datas inside
a = np.array([1,2,3,5,7], dtype='i')  #we specify the type of the numpy array, data type -> integers

b = np.array((2,3,4), dtype='f')      #data type - float





                                                    #NUMPY DIMENSIONS

a = np.array([[1,2,3],[4,5,6]])
print("a.ndim is : ",a.ndim)  #we get the array dimensions

b = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [1,2,3],
        [4,5,6]
    ]
])
print("b.shape is: ", b.shape)
print("b.shape[0] is: ", b.shape[0],"b.shape[1] is: ", b.shape[1],"b.shape[2] is: ", b.shape[2])

print("b[1,0,2] is : ", b[1,0,2]) #Same as b[1][0][2]
print(b[1][0][2])


#Check the total number of elements inside a numpy array
print(b.size)

