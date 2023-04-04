
#We need to import in order to use| Series are Similar to Arrays but we can also specify the indexes

from pandas import DataFrame
from pandas import Series

# this is how we declare it | If we dont give indexes by default it gives values starting from 0
se = Series([1,3,4,5])

# this is the way we access it
print(se[1])

# specify the indexes of our own choise
se2 = Series([100,200,300], index=['a','b','c'])

# print element with index 'a'
print(se2['a'])

# get all elements from indexes a - c(included)
print('Slicing 1: ',se2['a':'c'])

# we can also slice similar to numpy arrays or lists
print('Slicing 2: ',se2[0:2])

# convert Dictionary to Series
salary = {"John": 15000,"Tim":5000,"Gen":3200}
se3 = Series(salary)
print(se3)

# access Employee Salary by giving the name
print(se3['John'])

# print all the values
print(se3.values)

# print all the keys/indexes
print(se3.index)

