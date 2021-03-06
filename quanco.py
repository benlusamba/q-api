# Importing Quandl data for analysis (using Pandas)

import quandl
import pandas as pd
import csv                        # Allows importation/exporation of data as .csv file

gdp = quandl.get("FRED/GDP", authtoken="_uhAD1-g9JdY2teUwiAb")   # Import data using API call and applicable rules

print(gdp)                        # Show data in workspace

gdp.to_csv('gdp.csv')             # Export Data as .csv
