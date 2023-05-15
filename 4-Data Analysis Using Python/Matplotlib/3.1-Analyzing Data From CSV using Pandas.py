from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))



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
