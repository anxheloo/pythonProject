from matplotlib import pyplot as plt                      # -> Matplotlib Tutorials from Corey Schafer


# Here we can check all the styles available
print(plt.style.available)
# The style is just a layout for our graph and its elements to look a little different
plt.style.use('fivethirtyeight')

#  list of values we want for X values
ages_x = [25,26,27,28,29,30,31,32,33,34,35]
#  list of values we want for Y values
dev_y = [38496, 42000, 46687, 49123, 53123, 56123, 62123, 64123, 67317, 68748, 73123]
# We can add many arguments while plotting. For color we can also use hexvalue: color = '#444444'
plt.plot(ages_x,dev_y, color = 'k', linestyle='--',marker='.', label="All Devs",linewidth = 3)

# Adding another set of data into the same graph
python_dev_y = [45123,48123,53123,57123,63123,65123,70000,70123,71123,75123,83123]
# We can add many arguments while plotting.
plt.plot(ages_x,python_dev_y, color = 'b',marker='o', label="Python",linewidth = 2)

javaScript_dev_y = [37123,43123,46123,49123,53123,56123,62123,66234,68123,68657,74123]
plt.plot(ages_x,javaScript_dev_y, color='red', marker = '.', label = 'JavaScript',linewidth = 1)

plt.xlabel('Ages')                              #adding xlabel
plt.ylabel("Medium Salary (USD)")               #adding ylabel
plt.title('Median Salary (USD) by Age')         #adding title to the graph

'''
 plt.legend(["All Devs", "Python",'JavaScript'])
 To Distinguish the data shown in the grapgh we need to label each of them using a legend. Adding labels following the order we plotted data.
 The problem with this is that we need to follow the order of the plotted data. So another way is to add a label argument on the data when ploted,
 for example: plt.plot(ages_x, python_dev_y, label = "Python"), and just call the legend like below but without arguments:
 plt.legend()
'''
plt.legend()

# Creates a grid layout inside the graph
plt.grid(True)

# Automatically adjusts the subplots and decorations within a figure so that they fit neatly within the boundaries of the figure canvas.
plt.tight_layout()

plt.savefig('plot.png')

# if we want our data to show, we run this command
plt.show()



