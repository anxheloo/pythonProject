import pandas as pd
from matplotlib import pyplot as plt

# 1- We are reading data2.csv file using pandas
data = pd.read_csv('data2.csv')

# 2- We save column 'age' of data file to ages
ages = data['Age']

# 3- We save column 'All_Devs' of data file to dev_salaries
dev_salaries = data['All_Devs']

# 3- We save column 'Python' of data file to py_salaries
py_salaries = data['Python']

# 3- We save column 'JavaScript' of data file to js_salaries
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',linestyle='--', label='All Devs')
plt.plot(ages, py_salaries,label='Python')

overall_median = 57287

'''
4- We use fill_between function to fill the graph of the line for python_salaries. Alpha is used as an opacity
5 - overall_median and where = () function help us  fill the graph where python_salaries are grater than overall_median number.
  - interpolate=True helps us fill the graph correctly, without interceptions
  
  
plt.fill_between(ages, py_salaries,overall_median , where=(py_salaries > overall_median),interpolate=True, alpha = 0.25)
plt.fill_between(ages, py_salaries,overall_median , where=(py_salaries <= overall_median),interpolate=True, alpha = 0.25, color = "blue")
'''


'''
Instead of using overall_median as a fill_between avarage point, we use below dev_salaries
'''
plt.fill_between(ages, py_salaries,dev_salaries , where=(py_salaries > dev_salaries),interpolate=True, alpha = 0.25, label= 'Above Avg')
plt.fill_between(ages, py_salaries,dev_salaries , where=(py_salaries <= dev_salaries),interpolate=True, alpha = 0.25, color = "blue", label = 'Below Avg')


plt.legend()
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()
plt.savefig('fillingAreaOnLinePlots')
plt.show()