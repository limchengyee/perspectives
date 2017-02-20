import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pandas import Series, DataFrame
from datetime import datetime

#1(a)
#importing data
chicago = pd.read_csv('chicago.csv', sep = ',', usecols = ['DATE', 'TMAX', 'TMIN'], parse_dates = ['DATE'])
dc = pd.read_csv('dc.csv', sep = ',', usecols = ['DATE', 'TMAX', 'TMIN'], parse_dates = ['DATE'])
indiana = pd.read_csv('indianapolis.csv', sep = ',', usecols = ['DATE', 'TMAX', 'TMIN'], parse_dates = ['DATE'])
pittsburgh = pd.read_csv('pittsburgh.csv', sep = ',', usecols = ['DATE', 'TMAX', 'TMIN'], parse_dates = ['DATE'])
miami = pd.read_csv('miami.csv', sep = ',', usecols = ['DATE', 'TMAX', 'TMIN'], parse_dates = ['DATE'])

#merging miami, indiana, pittsburgh, washington into one dataframe
merged = dc.append(indiana)
merged = merged.append(pittsburgh)
merged = merged.append(miami)

# remove missing values
chicago = chicago[chicago['TMAX']>-9998]
chicago = chicago[chicago['TMIN']>-9998]
merged = merged[merged['TMAX']>-9998]
merged = merged[merged['TMIN']>-9998]

# modifying dates into datetime format
chicago['DATE'] = pd.to_datetime(chicago['DATE'])
merged['DATE'] = pd.to_datetime(merged['DATE'])

# create columns to make it easier to manipulate the data to get x-axis to be just one year
chicago['axis'] = chicago['DATE'].dt.dayofyear
chicago['year'] = chicago['DATE'].dt.year
chicago['monthday'] = chicago['DATE'].dt.month*100+chicago['DATE'].dt.day
merged['axis'] = merged['DATE'].dt.dayofyear
merged['year'] = merged['DATE'].dt.year
merged['monthday'] = merged['DATE'].dt.month*100+merged['DATE'].dt.day

# creating leap year list
i = 1976
leap_years = []
while i <= 2016:
    i += 4
    leap_years.append(i)

# creating non-leap year list
non_leap = []
i = 1976
#left out 1975, because it is the first year to define merged_all
#leave out 1976 manually because of the way leap_year is defined
for i in range(1976, 2017):
    if i not in leap_years:
        if i != 1976:
            non_leap.append(i)
            i += 1

#create a dataframe of leapyears for chicago
chicago_leap = chicago[chicago['year']==1976]
for i in leap_years:
    chicago_leap = chicago_leap.append(chicago[chicago['year']==i])

#create a dataframe of leapyears for rest of the cities
merged_leap = merged[merged['year']==1976]
for i in leap_years:
    merged_leap = merged_leap.append(merged[merged['year']==i])

#create a dataframe of non-leapyears for rest of the cities
merged_all = merged[merged['year']==1975]
for i in non_leap:
    merged_all = merged_all.append(merged[merged['year']==i])

#create a dataframe of non-leapyears for chicago
chicago_all = chicago[chicago['year']==1975]
for i in non_leap:
    chicago_all = chicago_all.append(chicago[chicago['year']==i])

#making axis(plotting as x-axis) different for leap and non-leap years
i = 100
while i < 922:
    i += 1
    chicago_all['axis'] = np.where(chicago_all['monthday']==i, chicago_all['axis'].add(365), chicago_all['axis'])
    chicago_leap['axis'] = np.where(chicago_leap['monthday']==i, chicago_leap['axis'].add(366), chicago_leap['axis'])
    merged_all['axis'] = np.where(merged_all['monthday']==i, merged_all['axis'].add(365), merged_all['axis'])
    merged_leap['axis'] = np.where(merged_leap['monthday']==i, merged_leap['axis'].add(366), merged_leap['axis'])

# append leap years and non leap years back to the same dataset
merged = merged_all.append(merged_leap)
chicago = chicago_all.append(chicago_leap)

#1(b)
#creating plotting x and y variables
merged_min = merged['TMIN']
merged_max = merged['TMAX']
merged_all = merged['TMIN'].append(merged['TMAX'])
chicago_max = chicago['TMAX']
chicago_min = chicago['TMAX']
chicago_all = chicago['TMIN'].append(chicago['TMAX'])
chicagod = chicago['axis'].append(chicago['axis'])
mergedd = merged['axis'].append(merged['axis'])

#plotting graph
width = 11.5
height = 6
ax, fig = plt.subplots(figsize=(width,height))
#1(c)
#plotting rest of the cities with black markers
plt.scatter(mergedd, merged_all, color='black', label='Other cities', s=0.01)
#1(d)
#plotting chicago data with maroon marker
plt.scatter(chicagod, chicago_all, color='maroon', label='Chicago', s= 0.01)
#zooming on x-axis values with plots
plt.xlim(264,629)

#1(e)
#color born in yellow
born = merged[merged['DATE']=='1975-01-22']
born_max = born['TMAX']
born_min = born['TMIN']
born_all = born_max.append(born_min)
bornd = born['axis'].append(born['axis'])
plt.scatter(bornd, born_all, color='yellow', label='Born', s=1, lw=4, edgecolor='black')

#color little league all-stars team championship
allstar = merged[merged['DATE']=='1988-07-14']
allstar_max = allstar['TMAX']
allstar_min = allstar['TMIN']
allstar_all = allstar_max.append(allstar_min)
allstard = allstar['axis'].append(allstar['axis'])
plt.scatter(allstard, allstar_all, color='yellow', label='allstar', s=1, lw=4, edgecolor='black')

#creating labels
plt.annotate('Born', xy=(387, 45), xytext=(384, 90),
            arrowprops=dict(facecolor='black', shrink=0.01, width=1)
            )
plt.annotate('Allstar regional championship', xy=(562, 66), xytext=(534, 30),
            arrowprops=dict(facecolor='black', shrink=0.01, width=1)
            )
            
#1(f) labelling graph
plt.title('Lifetime temperature', fontsize=15)
plt.xlabel(r'Year')
plt.ylabel(r'Temperature')
plt.legend(bbox_to_anchor=(1.2, 1), loc='upper right', prop={'size':10}, ncol=1)

#creating markers for x-axis labels
my_xticks = ['Autumn','Winter','Spring','Summer']
x = np.linspace(264,629,4)
plt.xticks(x, my_xticks)
