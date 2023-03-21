from pandas import Series

series = Series([100,200,300], index=['a','b','b'])
print(series)

#Identify with a boolean value if our indexes are unique or not 
print(series.index.is_unique)