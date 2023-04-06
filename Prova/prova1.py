'''Stock Price predictor
'''

import numpy as np
import pandas as pd

import yfinance as yf

import seaborn as sns
import matplotlib.pyplot as plt


stocks = input("Enter the code of the stock:- ")

# data = yf.download(stocks, "2022-01-01", "2022-03-03",auto_adjust=True)
# print(data.head())

msft = yf.Ticker(stocks)

# get all stock info (slow)
print(msft.info)

# fast access to subset of stock info (opportunistic)
print(msft.fast_info)

# get historical market data
hist = msft.history(period="1mo")
print(hist)

# - accurate time-series count:
a = msft.get_shares_full(start="2008-01-01", end="2021-01-18")
print("this is : ", a)


