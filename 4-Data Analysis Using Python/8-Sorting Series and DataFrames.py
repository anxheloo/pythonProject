from pandas import Series,DataFrame

series = Series([3,7,1,4,7,2], index=[2,7,3,5,9,1])
print(series)

#Sort Series by Index
sorted_series_by_index = series.sort_index()
print(sorted_series_by_index)

#Sort Series by its Values
sorted_series_by_values = series.sort_values()
print(sorted_series_by_values)



#                                     SORT DATAFRAMES
data = {'Speed':[101,109,106],'Temp':[34,23,42],'Humidity':[45,23,58]}
frame = DataFrame(data)

#Reindex the frame indexes
frame = frame.reindex([2,1,0])
print(frame)

#Sort data frames by Indexes
sorted_frame = frame.sort_index()
print(sorted_frame)

#Reindex Frame Columns
frame = frame.reindex(columns = ['Temp','Humidity','Speed'])
print(frame)

#Sort by Columns
sorted_frame_by_columns = frame.sort_index(axis=1)
print(sorted_frame_by_columns)

#Sort by Columns in Descending order
frame = frame.sort_index(axis=1,ascending=False)
print(frame)

#Sort DataFrames by its Values | We specify the Column Index in witch we want to sort
frame = frame.sort_values(by='Humidity')
print(frame)