'''
Bars used to represent continuous class intervals. For Example: How many pens sold in a price range from x=[10-20, 20-30, 30-40, 40-50]
                                                                                                         y=[15, 20, 30, 25, 5]
'''

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data3.csv')
ids = data['Responder_id']
ages = data['Age']

# bins is like x axis, for example: we can see that almoast 40.000 of our age data is between 20-30
bins=[10, 20,30,40,50,60,70,80,90,100]
plt.hist(ages, bins=bins,edgecolor='black',log=True)  # log=True helps us plot this graph on logarithmic scale, used when we have a lot of datas

median_age = 29
color = '#fc4f30'

# We use this to plot the median line of the responses. After calculating it was = 29
plt.axvline(median_age, color = color, label = 'Age Median')
plt.legend()
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.tight_layout()
plt.savefig('Histogram')
plt.show()