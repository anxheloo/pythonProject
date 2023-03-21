from pandas import Series,DataFrame

#1-Create a Serie
series = Series([100,200,300], index=['Speed','Temp','Humidity'])
print(series)

#2-Create a DataFrame
data = {'Speed':[101,109,106],'Temp':[34,23,42],'Humidity':[45,23,58]}
frame = DataFrame(data)

#3-Submission between a DataFrame and a Serie | Every element in Each Category of the frame will be deducted with the Index that equals in name.
                                             #| Each Element in Speed Category of the frame with be deducted by the element in Speed Index of the serie.
result = frame - series
print(result)


#4-Submission between a DataFrame with 3 Categories and a Serie with 2 Indexes | It will perform operations as above except it will add NaN at missing field
series2 = Series([100,200], index=['Speed','Temp'])
result2 = frame - series2
print(result2)
