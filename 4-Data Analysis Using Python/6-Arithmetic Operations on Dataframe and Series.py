from pandas import Series,DataFrame

#1-Working with Series

series1 = Series([1,2,3,4,5])
series2 = Series([100,200,300,400,500])

#2-Lets perform addition
result = series1 + series2
print(result)

#If we have more elements in a serie and try to add them, the result at index of element that is more will display NaN
series3 = Series([1,2,3,4,5])
series4 = Series([100,200,300,400,500,600])
result2 = series3 + series4
print(result2)

print()
print()



#3-Working with DataFrames
data1 = {'Speed':[100,103,105],'Temp':[34,23,42]}
frame1 = DataFrame(data1)
print(frame1)

print()
print()

data2 = {'Speed':[101,109,106],'Temp':[34,23,42],'Humidity':[45,23,58]}
frame2 = DataFrame(data2)
print(frame2)

#4-Printing the Addition of frame1 and frame2 | In this case we have 1 more column at frame2("Humidity"), It will add up same columns and put NaN at Humidity
result3 = frame1 + frame2
print(result3)

