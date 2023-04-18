import matplotlib.pyplot as plt
import numpy as np

# create some datas staring from 0-10 with 1000 points evenly spaces between
x = np.linspace(0,10,1000)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# scatter is a graph with points, we pick every element of x & y, but with a step of 10
plt.scatter(x[::10],y[::10],color='red')
plt.show()

'''
    Other attributes we can add '-g' -> solid green
                                '--c' -> dashed cyan
                                '-.k' -> dashdot black
                                ':r' -> dotted red
                                '-'  -> solid line
                                '--' -> dotted line
                                'o-' -> solid line with markers for every point
'''