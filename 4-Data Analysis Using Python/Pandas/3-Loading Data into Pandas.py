import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

'''
Read & Load
'''

# 1.Load data from a csv file
mydata = pd.read_csv('pokemon_data.csv')
print(mydata.head(3)) # -> .head() function helps us print only the rows we specify starting from head
print(mydata.tail(3)) # -> .tail() function helps us print only the rows we specify starting from end

# 2.Load Data from Excel file
myExcelData = pd.read_excel('pokemon_data.xlsx')
print(myExcelData.head(3))
print(myExcelData.tail(3))

# 3.Loading Data from txt file
mytxtdata = pd.read_csv('pokemon_data.txt', delimiter="\t")   # we use tab_separated values as a delimiter
print(mytxtdata.head(3)) # -> .head() function helps us print only the rows we specify starting from head
print(mytxtdata.tail(3))

# 4.Read Headers (Columns name)
print(mydata.columns)

# 5.Read a Specific Column
print('Read a Specific Column')
print(mydata['id'])
# Read Top Five rows of a specific column
print(mydata['Name'][0:5])

# 6.Read a Specific Row
print('Read a Specific Row')
print(mydata.iloc[1]) # iloc stands for integer location
# Get multiple Rows
print(mydata.iloc[0:5])

# 7. Read a Specific Location in this case: read from mydata at row index = 1, column index = 1 .
print(mydata.iloc[1,1])


'''
Iterate
'''

# 8. Iterate over the data frame.
for index, row in mydata.iterrows():
    print(index, row)

# Iterate and print only the datas in column 'Name'
for index, row in mydata.iterrows():
    print(index,row['Name'])

# 9.Filter mydata file to print only the rows where Column 'Speed' == 100
print(mydata.loc[mydata['Speed'] == 100])


'''
Sorting/Describing Data
'''

# 1.describe() function gives us some datas: mean, standard deviation, etc
print(mydata.describe())

# 2.Sort values by column 'Name' in alphabetic order
print(mydata.sort_values('Name'))
# This makes it Descending
print(mydata.sort_values('Name', ascending=False))
# We can also sort by giving more than 1 Column as reference, and also specify the ascending or descending order
print(mydata.sort_values(['Type 1', "HP"], ascending=[1,0]))


'''
Making Changes to Data
'''
# 1.Adding another column named "Total" that is = to the sum of all the below columns | Way 1
mydata['Total'] = mydata['HP'] + mydata["Attack"] + mydata["Defense"] + mydata["Sp. Atk"] + mydata["Sp. Def"] + mydata["Speed"]
print(mydata.head(5))

# Drop a Specific Column
mydata = mydata.drop(columns='Total')
print(mydata)

# 1.Adding another column named "Total" that is = to the sum of all the below columns | Way 2
mydata['Total'] = mydata.iloc[:, 4:9].sum(axis=1)
print(mydata)


'''
Change the Order of Columns
'''
mydata = mydata.reindex(columns=['Name','id', "Type 1","Legendary","Total","HP","Attack","Defense","Sp. Atk","Sp. Def", "Speed" ])
print(mydata)


'''
Save Modified File as csv file
'''
mydata.to_csv("modifiedColumns.csv", index=False)  # index = False -> we dont save the index of rows with our file
mydata.to_excel("modifiedColumns.xlsx")
mydata.to_csv("modifiedColumns.txt", sep="\t")


'''
Filtering Data - even that we filter, the index of rows still remainds the same, so we need to reset them using reset_index() function
'''
# 1.
print(mydata.loc[mydata["Type 1"] == 'Grass'])      # -> print rows where Type 1 = Grass
newData = mydata.loc[(mydata["Type 1"] == 'Grass') & (mydata['Speed'] == 100)] # filter and save datas where Type 1 = Grass & Speed = 100
newData = newData.reset_index()
print(newData)

# 2. Filter Datas where they contain the word 'Mega' in the column 'Name'
filtered2 = mydata.loc[mydata['Name'].str.contains('Mega')]
filtered2 = filtered2.reset_index()
print(filtered2)

# 3. '~' sign is same as 'not' , in this example we are filtering and selecting rows that doesnt include work 'Mega' in the column 'Name'
filtered3 = mydata.loc[~mydata['Name'].str.contains('Mega')]
print(filtered3)

# 4. Using regex functions
filtered4 = mydata.loc[mydata['Type 1'].str.contains('Fire|Grass', regex=True)]
# filtered4 = mydata.loc[mydata['Type 1'].str.contains('fire|grass',flags=re.I, regex=True)]  Ignore UpperCase with flags=re.I
print(filtered4)


'''
Conditional Changes  - > Study more if needed!
'''
filtered5 = mydata.loc[mydata['Type 1'] == 'Fire', 'Legendary'] = True
print(filtered5)


'''
Group By function
'''

# Group by 'Type 1', find the mean() of all the values and sort them by 'Attack'
print(mydata.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))


