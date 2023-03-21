#We need to import in order to use| Serieas are Similar to Arrays but we can also specify the indexes
from pandas import Series

#1-This is the way we declare it
se = Series([1,3,4,5])

#2-This is the way we use it
print(se[1])

#3-Specify the indexes of our own choise
se2 = Series([100,200,300], index=['a','b','c'])
print(se2['a'])

#4-Convert Dictionary to Series
salary = {"John": 15000,"Tim":5000,"Gen":3200}
se3 = Series(salary)
print(se3)

#Access Employee Salary by giving the name
print(se3['John'])