# Importing Quandl data for analysis (using Pandas)
import quandl
import random
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np

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

#Distribution of Logs:
plt.hist(a, bins='auto', orientation='vertical')
plt.title('Distribution of Logs')
plt.ylabel('Frequency')
plt.xlabel('Log Values - 322 Observations')
plt.show()

#Box Plot:
plt.boxplot(a)
plt.title('Outliers')
plt.show()
