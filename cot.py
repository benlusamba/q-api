# Importing Quandl data for analysis (using Pandas, Matplotlib)
import quandl
import matplotlib as plt
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from pandas import DataFrame
from pandas import Series
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.stattools import adfuller

cot = quandl.get("CFTC/005602_FO_ALL", authtoken="Your_Key_HERE")

print(cot)                                         # Show data in workspace

cot.to_csv('cot.csv')                              # Export Data as .csv

df1 = pd.read_csv('cot.csv')

z = df1['Date'].values
x = df1['Open Interest'].values

#Now for some data visualization:
plt.plot(z, x, c = 'orange')                                    # Plot
axes = plt.gca()                                                # Define axes
#plt.ylim(500000, 1096288)                                      # Set y axis limits
plt.gcf().autofmt_xdate()                                       # beautify the x-labels

# Adjust axis scales
#axes.set_yticks(axes.get_yticks()[::5000])
axes.set_xticks(axes.get_xticks()[::25])

#Label graph, and show:
plt.title('Soybean Open Interest')
#plt.ylabel('Open Interest')
plt.show()

a = np.log(x)
plt.plot(z, a, c = 'green')
axes = plt.gca()
plt.gcf().autofmt_xdate()
axes.set_xticks(axes.get_xticks()[::25])
plt.title('Log of Soybean OI')
plt.show()

# Change of Change:

b = np.log(a)
plt.plot(z, b, c = 'purple')
axes = plt.gca()
plt.gcf().autofmt_xdate()
axes.set_xticks(axes.get_xticks()[::25])
plt.title('OI Volatility')
plt.show()

#Plot the distribution of Logs:
plt.hist(a, bins='auto', orientation='vertical')
plt.title('Distribution of Logs')
plt.ylabel('Frequency')
plt.xlabel('Log Values - 322 Observations')
plt.show()

#Box Plot of the distribution of the logs to spot outliers:
plt.boxplot(a)
plt.title('Outliers')
plt.show()

print(" ")
print("Forcasting OI")

series = read_csv('oi.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(1,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
plt.title('OI Forecast - predictions red')
pyplot.show()
