from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

'''
The problem with including multiple bar charts inside a figure is: longest datas will be covering the shorter ones. To solve this we use numpy:
1-We create a numpy array that hold the indexes of the x data.
2-We replace ages_x with x_indexes
3-We create a variable width, we can play with its value
4-We move first bar to the left: x_indexes - width, let the middle bar as it is, move the third bar to the right:  x_indexes + width,
5-We set the width of each bar to the width variable, so we can see all of them 3 around a single point 
'''

ages_x = [25,26,27,28,29,30,31,32,33,34,35]
x_indexes = np.arange(len(ages_x))
width = 0.25


dev_y = [38496, 42000, 46687, 49123, 53123, 56123, 62123, 64123, 67317, 68748, 73123]
plt.bar(x_indexes - width,dev_y,width = 0.25, label="All Devs")

python_dev_y = [45123,48123,53123,57123,63123,65123,70000,70123,71123,75123,83123]
plt.bar(x_indexes,python_dev_y,width = 0.25, color = 'blue', label="Python")

javaScript_dev_y = [37123,43123,46123,49123,53123,56123,62123,66234,68123,68657,74123]
plt.bar(x_indexes + width, javaScript_dev_y,width = 0.25, color = 'yellow', label = 'JavaScript',linewidth = 1)



plt.legend()

'''
When we used the x_ages indexes to our bar chart we no longer can see the age, but only the indexes. Thats why 
we use this function to set the x-es with labels: ages_x
'''
plt.xticks(ticks=x_indexes, labels=ages_x)

plt.xlabel('Ages')
plt.ylabel("Medium Salary (USD)")
plt.title('Median Salary (USD) by Age')

plt.tight_layout()
plt.savefig("BarChart")
plt.show()
