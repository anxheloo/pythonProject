import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


'''
1.Plot Single Points in 3D:

ax1 = plt.axes(projection='3d')
ax1.scatter(5,6,7, marker='v')
plt.show()
'''


'''
2.Plot Multiple Points in 3D:

ax2 = plt.axes(projection='3d')
x_data = np.random.randint(0,100, (500,))
y_data = np.random.randint(0,100, (500,))
z_data = np.random.randint(0,100, (500,))
ax2.scatter(x_date,y_date,z_date, marker='v')
plt.show()
'''

'''
3.Plotting a Function on 3d

ax = plt.axes(projection='3d')
x_data = np.arange(0,50,0.1)
y_data = np.arange(0,50,0.1)
z_data = x_data * y_data
ax.plot(x_data,y_data,z_data)
ax.set_title('Funny Function')
ax.set_xlabel('My x values in cm')
ax.set_ylabel('My y values in cm')
ax.set_zlabel('My result')
plt.show()
'''

# 4.Surface Plots 3D
ax = plt.axes(projection = '3d')
x_data = np.arange(0,50,0.1)
y_data = np.arange(0,50,0.1)

X,Y = np.meshgrid(x_data,y_data)
Z = X * Y
ax.plot_surface(X,Y,Z, cmap='plasma') # cmap -> the higher the values the more yellow they are and the lower the values the more purple
plt.show()
print(X)
print(X[1,2])