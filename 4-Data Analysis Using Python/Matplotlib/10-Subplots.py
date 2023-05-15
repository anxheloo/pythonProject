import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data2.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# Plot 2 Graphs on 2 different Figures
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# 1- Plot first graph of the first figure
ax1.plot(ages, dev_salaries, color='#444444',linestyle='--', label='All Devs')

# 2- Plot second graph of the second figure
ax2.plot(ages, py_salaries, label='Python')
# 3- Plot third graph of the second figure
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()
fig1.savefig('fig1.png')
fig2.savefig('fig2.png')



'''
Plot 3 graphs inside 1 Figure:

fig, (ax1, ax2, ax3) = plt.subplots(3,1)
ax1.plot(ages, dev_salaries, color='#444444',linestyle='--', label='All Devs')
ax2.plot(ages, py_salaries, label='Python')
ax3.plot(ages, js_salaries, label='JavaScript')

plt.legend()

plt.suptitle('Median Salary (USD) by Age')  -> Main Title for the whole figure
ax3.set_xlabel("Ages")      -> set xlabel on a specifi graph inside the figure
plt.xlabel('Ages')          -> set xlabel for the whole figure

plt.ylabel('Median Salary (USD)')       -> set ylabel for the whole figure
ax1.set_ylabel('Median Salary (USD)')   -> set ylabel for graph ax1 inside the figure
ax2.set_ylabel('Median Salary (USD)')   -> set ylabel for graph ax2 inside the figure
ax3.set_ylabel('Median Salary (USD)')   -> set ylabel for graph ax3 inside the figure
'''


'''
Multiple graphs in 1 figure : 

fig, axes = plt.subplots(3,2, figsize = (12,12))
ax = axes[0][0]
ax.plot(x, y, 'o--')
ax.set_xlabel('asd')
ax.set_ylabel('asddds')

ax = axes[0][1]
ax.set_xlabel('asd')
ax.set_ylabel('asddds')

ax.legend()
ax.set_title('Histrogram')
plt.show()
'''