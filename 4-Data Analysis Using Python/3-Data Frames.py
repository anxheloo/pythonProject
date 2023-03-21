#Like Series they are Data Structures but main difference is that Series has 1 index, Data Frames have 2 indexes(row index & column index)

#1-Import Data Frames
from pandas import DataFrame

#2-Create a data frame for 3 employees with Name,Age,Salary
data = {'Name':['John','Tim','Rob'],
        'Age':[34,23,42],
        'Salary':[4500,2300,5800]}


#3-Create a frame object, we use the DataFrame method and give it the 'data' we created and store it in a variable
frame = DataFrame(data)
print(frame)

#4-Specify the Column Sequence(Instead of 'Name', 'Age', 'Salary' we specify to arrange columns as: 'Age', 'Name', 'Salary')
new_frame = DataFrame(data,columns=['Age','Name','Salary'])
print(new_frame)

#5-If we try to add another column, it will be added with 'NaN' in every row
add_new_column = DataFrame(data,columns=['Age','Name','Salary','Profile'])
print(add_new_column)

#6-Retrieve data as series from data frames | Lets say we want to print only the Salary column from new_frame
print(new_frame['Salary'])

#7-Modify the profile column in add_new_column| In this case every one will be a doctor
add_new_column['Profile'] = 'Doctor'
print(add_new_column)

#8-If we try dto modify smthng that does not exist, it will add it and update every row field with the value we specify
add_new_column['Education'] = "MS"
print(add_new_column)

#9-Convert Rows to Columns and Columns to Rows
add_new_column = add_new_column.T  #Execute this again to change things as they were before
print(add_new_column)


