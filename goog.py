import pandas as pd
import numpy as np
import pandas_datareader as web #pandas.io.data is deprecated 
import datetime #not imported
import matplotlib.pyplot as plt #not imported


#this block is not splicitly defined on the book
start_date = datetime.datetime(2018, 1, 1)
end_date = datetime.datetime(2023, 5, 12)

#dates are declared as follows, mixing web.DataReader and dates:
#goog = web.DataReader('GOOG', data_source='google',

start='3/14/2009', end='4/14/2014')
goog = web.DataReader('GOOG', 'stooq', start_date, end_date)
goog = web.DataReader('GOOG', 'stooq', start_date, end_date)

goog.tail()
goog.head()

goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
goog['Volatility'] = pd.rolling_std(goog['Log_Ret'], window=252) * np.sqrt(252)
#pd.rolling_std doesn't exist on python3
goog[['Close', 'Volatility']].plot(subplots=True, color='blue',
figsize=(8, 6))


