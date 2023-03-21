from pandas import DataFrame

#10-Delete Rows & Columns from Data Frame



data = {'Name':['John','Tim','Rob'],
        'Age':[34,23,42],
        'Salary':[4500,2300,5800]}

frame = DataFrame(data)
print(frame)

#Remove Row at index 2
frame2 = frame.drop([2])
print(frame2)

#Remove Column
frame3 = frame.drop('Salary',axis = 1)  #axis = 1 is used when dropping a column
print(frame3)



