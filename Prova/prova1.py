'''
Boston House Price Prediction Project - We used california cuz boston dataset was not anymore available
In this project you will work on developing an end to end machine learning project using linear regression, as this will be your first
project in your machine learning journey. We will be doing extensive data visualization, we will perform data feature engineering, we will also see
how we can select features based on the correlation of the features
'''

import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates

import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn.datasets import fetch_california_housing
fetch_california_housing = fetch_california_housing()
x = fetch_california_housing.data
y = fetch_california_housing.target

data = pd.DataFrame(x, columns=fetch_california_housing.feature_names)  #Building a dataframe giving x(indipendent variable), with column name specified
data["SalePrice"] = y     #saleprice
# data.head()

print(data.head())
print(fetch_california_housing.DESCR)
print(data.shape)
print(data.info())
print(data.describe())



