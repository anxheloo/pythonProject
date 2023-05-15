import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

'''
    It creates a scatter plot using Matplotlib library where the 'view_count' is plotted against the 'likes', 
    and the color of the scatter points is determined by the 'ratio'.
    The color of the points is chosen using the 'summer' color map, and the points are outlined with a black color, and their linewidths are set to 1. 
    The transparency of the points (alpha) is set to 0.5.
    Next, a color bar is added to the plot using the 'colorbar' function, and its label is set to 'Like/Dislike Ratio'.
'''

data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count,likes,c = ratio, cmap='summer', edgecolor='black',linewidths=1,alpha=0.5)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

# Now we can see the correlation better
plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()