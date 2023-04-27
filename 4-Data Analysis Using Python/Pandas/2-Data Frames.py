


# Like Series they are Data Structures but main difference is that Series has 1 index,
# Data Frames have 2 indexes(row index & column index)

from pandas import DataFrame
import pandas as pd

# create a data frame for 3 employees with Name,Age,Salary

data = {'Name':['John','Tim','Rob'],
        'Age':[34,23,42],
        'Salary':[4500,2300,5800]}

frame = DataFrame(data)
print(frame)

# rearrange keys
new_frame = DataFrame(data,columns=['Age','Name','Salary'])
print(new_frame)

# if we try to add another column, it will be added with 'NaN' in every row
add_new_column = DataFrame(data,columns=['Age','Name','Salary','Profile'])
print(add_new_column)

# print only the Salary column from new_frame
print('printing Salary columns: ', new_frame['Salary'])

# print only the first element of the salary column | printing row: Salary , column: first element
print(new_frame['Salary'][0])

# modify the profile column in add_new_column
add_new_column['Profile'] = 'Doctor'
print(add_new_column)

# if we try to modify smthng that does not exist, it will add it and update every row field with the value we specify
add_new_column['Education'] = "MS"
print(add_new_column)

# convert Rows to Columns and Columns to Rows
add_new_column = add_new_column.T  #Execute this again to change things as they were before
print(add_new_column)



# create a dataFrame that has 2 series of dictionaries inside
grades_dictionary = {'A':4,'A-':3.5,'B':3,'B-':2.5,'B':2}
grades = pd.Series(grades_dictionary)

marks_dictionary = {'A':85,'A-':80,'B':75,'B-':70,'B':65}
marks = pd.Series(marks_dictionary)

myDataFrame = pd.DataFrame({'grades': grades_dictionary, 'marks': marks_dictionary})
print(myDataFrame)

# print column grades from myDataFrame
print(myDataFrame['grades'])

# print value of key: A in grades
print(myDataFrame['grades']['A'])

# print first value of grades
print(myDataFrame['grades'][0])

# print values from 0-2(exclusive) from all dictionaries inside myDataFrame
print(myDataFrame[:][0:2])

# using .iloc is the same slicing tecnique as numpy
print(myDataFrame.iloc[0:2,0:2])




