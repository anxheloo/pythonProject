from pandas import DataFrame,Series
import numpy as np


# SERIES

series = Series([1,2,3,4,np.nan],index=['a','b','c','d','e'])
print(series)

#Drop the NaN values
series = series.dropna()
print(series)


#DATA FRAMES
data = {'Speed':[101,np.nan,106],'Temp':[34,23,42],'Humidity':[4500,np.nan,5800]}
frame = DataFrame(data)
print(frame)

#To drop the NaN values: It completely removes the rows in which NaN values exists
frame1 = frame.dropna()
print(frame1)

#Every NaN value will be replaced by 0 | We can whatever replacement we want
frame2 = frame.fillna(0)
print(frame2)

