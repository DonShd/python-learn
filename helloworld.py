from behold import Behold
from collections import deque
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
#tickers = ['AAPL', 'MSFT', '^GSPC']

# Define which online source one should use
#data_source = 'morningstar'
symbol = 'HKEX/00700'
# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2016-12-20'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
# panel_data = data.DataReader(tickers, data_source, start_date, end_date)
df = data.DataReader(symbol, 'quandl', '2017-01-05', '2017-02-05')
print (df)