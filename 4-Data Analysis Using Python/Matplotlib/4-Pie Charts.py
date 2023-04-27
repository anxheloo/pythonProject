from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

slices = [38496, 42000, 46687, 49123, 53123]     # percentage of pies
labels = ['JavaScript', 'HTML/CSS','SQL','Python','Java']  # labels for pies

'''
 We can create a color list and store different colors for our datas, and add color attribute in our pie: plt.pie(color = colors)
  -> colors = ['blue','red','yellow','green']
'''

'''
 We can create an explode list and specify the element in which we want to seperate a little bit, in this case we want to separate people who know python. 
 So python is 4th element of labels list, so in our explode list we set the 4th element to 0.1 meaning 10 percent from the radious.
'''
explode = [0,0,0,0.1,0]

'''
wedgeprops is an element used to give a solid line around the pies and the graph. Like a line for the edge.
explode is used to seperate a piece of the pie
startangle is used to rotate the pie an start in a different angle
autopct is used to show the % of the pies in the graph
'''
plt.pie(slices,labels = labels, wedgeprops={'edgecolor':'black'},explode = explode, shadow= True , startangle=90, autopct='%1.1f%%')

plt.title('Pie Chart')
plt.tight_layout()
plt.savefig('pieChart')
plt.show()
