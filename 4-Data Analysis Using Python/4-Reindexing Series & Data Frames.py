from pandas import Series
from pandas import DataFrame

#1-Reindex Series
obj = Series([100,200,300,400,500],index=['d','a','b','e','c'])
print(obj)

#Reindexing the obj Series from index=['d','a','b','e','c'] -> ['a','b','c','d','e']
obj = obj.reindex(['a','b','c','d','e'])
print(obj)



#2-Reindex Data Frame
data = {'Name':['John','Tim','Rob'],
        'Age':[34,23,42],
        'Salary':[4500,2300,5800]}

frame = DataFrame(data)
print(frame)

frame = frame.reindex([0,2,1])          #Reindexing the row indexes
print(frame)

fields = ['Salary','Age','Name']
frame = frame.reindex(columns = fields) #Reindexing the Column indexes
print(frame)