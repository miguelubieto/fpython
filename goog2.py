import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf #used yfinance instaed of pandas_datareader
import numpy as np
style.use('ggplot')

start = dt.datetime(2018,5,31)
end = dt.datetime(2023,5,12)

goog = yf.download("GOOGL", start, end)

print(goog.head())
print(goog.tail())

#this block is the same as in the book
goog['Log_Ret'] = np.log(goog['Adj Close']/goog['Adj Close'].shift(1))

#however they print both the yf.download, the Log_Ret and then again the volatility after rolling 
print(goog.head()['Log_Ret'])
print(goog.tail()['Log_Ret'])

#using ".rolling instead of pd.rolling_std, applied to df (which is =yf.download), and in the book is using this function from .pd directly"

goog['Volatility'] = goog['Log_Ret'].rolling(window=252).std()*np.sqrt(252)

print(goog.head())
print(goog.tail())

goog.to_csv('GOOGL.csv')
goog[['Adj Close','Volatility']].plot(subplots=True,color='blue',figsize=(8,6))
plt.show()

