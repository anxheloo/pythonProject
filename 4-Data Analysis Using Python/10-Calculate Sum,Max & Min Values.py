from pandas import DataFrame

data = {'Speed':[101,109,106],'Temp':[34,23,42],'Humidity':[45,23,58]}
frame = DataFrame(data)
print(frame)

#Calculate Sum of Columns: Speed, Temp, Humidity and display them in a single value
frame1 = frame.sum()
print(frame1)

#Calculate the sum of the rows
frame2 = frame.sum(axis=1)
print(frame2)

#Check the maximum and minimum value in Columns by indexes
print(frame.idxmax())

print(frame.idxmin())