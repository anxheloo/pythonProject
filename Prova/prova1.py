import numpy as np
import matplotlib.pyplot as plt

print(plt.style.available)
# plt.style.use(['science','notebook','grid'])

x = np.linspace(0,15,30)
y = np.sin(x) + 0.1 * np.random.randn(len(x))
y1 = y + 1

# Change fig size
plt.figure(figsize=(8,3))
plt.plot(x,y,"o",label = 'component 1')
plt.plot(x,y1,"-",label = 'component 2')

# Make the legend horizontal
plt.legend(loc='upper right', fontsize=10, ncol=2)

plt.show()
