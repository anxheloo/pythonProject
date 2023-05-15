from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter

plt.style.use('fivethirtyeight')

'''
This code below used the csv module to read files from csv. We use data.csv we have in our project. We use the Counter module from collections 
to count the number of times an element is present. 

'''
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

# Here we print the first line of our data
    # row = next(csv_reader)
# We print the first line of the directory by keyword and splitting by ;
    # print(row['LanguagesWorkedWith'].split(';'))

# Here we update our counter by iterating each row
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))



print(language_counter)
# 15 most common responses, given as a tuple
print(language_counter.most_common(15))

# We want to plot this data , Languages and counts:

# 1 - Create 2 empty lists to store languages and counts
languages = []
popularity = []

# 2 - Iterate each tuple in language_counter and add first element of tuple(which is language) to languages & second element to popularity
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)
plt.ylabel('Programing Languages')
plt.xlabel("Number of People Who Use")
plt.title('Most Popular Languages')

plt.tight_layout()
plt.savefig('horizontalBarChart')
plt.show()
