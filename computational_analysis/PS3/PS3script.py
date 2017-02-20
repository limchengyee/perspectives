import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pandas import Series, DataFrame
from datetime import datetime
from mpl_toolkits.mplot3d import Axes3D


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
while i < 920:
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
plot = True

if plot:
    '''
    --------------------------------------------------------------------
    cur_path    = string, path name of current directory
    output_fldr = string, folder in current path to save files
    output_dir  = string, total path of images folder
    output_path = string, path of file name of figure to be saved
    xx          = (45,) vector, values of xx
    yy          = (45,) vector, values of yy
    --------------------------------------------------------------------
    '''
    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    #define dimensions of canvas
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
    plt.xlim(264,631)

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
    plt.annotate('Allstar regional championship', xy=(562, 66), xytext=(525, 30),
                arrowprops=dict(facecolor='black', shrink=0.01, width=1)
                )

    #1(f) labelling graph
    plt.title('Lifetime temperature', fontsize=15)
    plt.xlabel(r'Year')
    plt.ylabel(r'Temperature')
    plt.legend(bbox_to_anchor=(0.93, 0.3), loc='upper right', prop={'size':10}, ncol=1)

    #creating markers for x-axis labels
    my_xticks = ['Autumn','Winter','Spring','Summer']
    x = np.linspace(264,631,4)
    plt.xticks(x, my_xticks)

    output_path = os.path.join(output_dir, 'Q1scatter')
    plt.savefig(output_path)
    # plt.show()
    plt.close()


#Q2(a)
df = pd.read_csv("lipids.csv", header = 3, sep=',')

plot = True

if plot:
    '''
    --------------------------------------------------------------------
    cur_path    = string, path name of current directory
    output_fldr = string, folder in current path to save files
    output_dir  = string, total path of images folder
    output_path = string, path of file name of figure to be saved
    xx          = (45,) vector, values of xx
    yy          = (45,) vector, values of yy
    --------------------------------------------------------------------
    '''
    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    # Plot histogram of concentration of plasma cholesterol (mg/dl)
    chol = df[["chol"]]
    chol = chol.stack()
    num_bins = 25
    weights = (1 / chol.shape[0]) * np.ones_like(chol)
    n, bin_cuts, patches = plt.hist(chol, num_bins, weights=weights, facecolor='green')

    # for the minor ticks, use no labels; default NullFormatter
    plt.title('Histogram of concentration of plasma cholesterol (mg/dl)', fontsize=17)
    plt.xlabel(r'Concentration of plasma cholesterol (mg/dl)')
    plt.ylabel(r'Frequency')
    output_path = os.path.join(output_dir, 'chol_hist_2a')
    plt.savefig(output_path)
    # plt.show()
    plt.close()

#Q2(b)(c)
df = pd.read_csv("lipids.csv", header = 3, sep=',')
chol = df[["chol"]]
chol = chol.stack()
trig = df[["trig"]]
trig = trig.stack()

plot = True

if plot:
    '''
    --------------------------------------------------------------------
    cur_path    = string, path name of current directory
    output_fldr = string, folder in current path to save files
    output_dir  = string, total path of images folder
    output_path = string, path of file name of figure to be saved
    xx          = (45,) vector, values of xx
    yy          = (45,) vector, values of yy
    --------------------------------------------------------------------
    '''
    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    # Plot histogram of concentration of plasma cholesterol (mg/dl)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection ='3d')
    bin_num = int(9)
    hist, xedges, yedges = np.histogram2d(trig, chol, bins=bin_num)
    hist = hist / hist.sum()
    x_midp = xedges[:-1] + 0.5 * (xedges[1] - xedges[0])
    y_midp = yedges[:-1] + 0.5 * (yedges[1] - yedges[0])
    elements = (len(xedges) - 1) * (len(yedges) - 1)
    ypos, xpos = np.meshgrid(y_midp, x_midp)
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros(elements)
    dx = (xedges[1] - xedges[0]) * np.ones_like(bin_num)
    dy = (yedges[1] - yedges[0]) * np.ones_like(bin_num)
    dz = hist.flatten()
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='g', zsort='average')
    ax.set_xlabel('Concentration of triglycerides (mg/dl)')
    ax.set_ylabel('Concentration of cholesterol (mg/dl)')
    ax.set_zlabel('Frequency')
    plt.title('Histogram by Concentration of Plasma Triglycerides and Cholesterol')

    # for the minor ticks, use no labels; default NullFormatter
    output_path = os.path.join(output_dir, '3d_hist_2b')
    plt.savefig(output_path)
    # plt.show()
    plt.close()


#3(a)
recess = pd.read_csv("payems.csv", header = 5, parse_dates = ['date'])
recess['date'] = pd.to_datetime(recess['date'])
recess.index = recess['date']

#generating time period of 2007-12 recession
rec2007 = recess['2006-12']
x = recess[(recess['date'].dt.year>2006) & (recess['date'].dt.year<=2014)]
rec2007 = rec2007.append(x)

#generating time preiod of 2001-03 recession
x = recess[(recess['date'].dt.year > 2000) &
        (recess['date'].dt.year < 2008)]
rec2001 = recess['2000-03']
rec2001 = rec2001.append(recess['2000-04'])
rec2001 = rec2001.append(recess['2000-05'])
rec2001 = rec2001.append(recess['2000-06'])
rec2001 = rec2001.append(recess['2000-07'])
rec2001 = rec2001.append(recess['2000-08'])
rec2001 = rec2001.append(recess['2000-09'])
rec2001 = rec2001.append(recess['2000-10'])
rec2001 = rec2001.append(recess['2000-11'])
rec2001 = rec2001.append(recess['2000-12'])
rec2001 = rec2001.append(x)
rec2001 = rec2001.append(recess['2008-01'])
rec2001 = rec2001.append(recess['2008-02'])
rec2001 = rec2001.append(recess['2008-03'])

#generating time period of 1990-07 recession
x = recess[(recess['date'].dt.year > 1989) &
        (recess['date'].dt.year < 1997)]
rec1990 = recess['1989-07']
rec1990 = rec1990.append(recess['1989-08'])
rec1990 = rec1990.append(recess['1989-09'])
rec1990 = rec1990.append(recess['1989-10'])
rec1990 = rec1990.append(recess['1989-11'])
rec1990 = rec1990.append(recess['1989-12'])
rec1990 = rec1990.append(x)
rec1990 = rec1990.append(recess['1997-01'])
rec1990 = rec1990.append(recess['1997-02'])
rec1990 = rec1990.append(recess['1997-03'])
rec1990 = rec1990.append(recess['1997-04'])
rec1990 = rec1990.append(recess['1997-05'])
rec1990 = rec1990.append(recess['1997-06'])
rec1990 = rec1990.append(recess['1997-07'])

#generating time period of 1981-07 recession
x = recess[(recess['date'].dt.year > 1980) &
        (recess['date'].dt.year < 1988)]
rec1981 = recess['1980-07']
rec1981 = rec1981.append(recess['1980-08'])
rec1981 = rec1981.append(recess['1980-09'])
rec1981 = rec1981.append(recess['1980-10'])
rec1981 = rec1981.append(recess['1980-11'])
rec1981 = rec1981.append(recess['1980-12'])
rec1981 = rec1981.append(x)
rec1981 = rec1981.append(recess['1988-01'])
rec1981 = rec1981.append(recess['1988-02'])
rec1981 = rec1981.append(recess['1988-03'])
rec1981 = rec1981.append(recess['1988-04'])
rec1981 = rec1981.append(recess['1988-05'])
rec1981 = rec1981.append(recess['1988-06'])
rec1981 = rec1981.append(recess['1988-07'])

#generating time period of 1980-01 recession
rec1980 = recess[(recess['date'].dt.year >= 1979) &
        (recess['date'].dt.year < 1987)]
rec1980 = rec1980.append(recess['1987-01'])

#generating time perod of 1973-11 recession
x = recess[(recess['date'].dt.year > 1972) &
        (recess['date'].dt.year < 1980)]
rec1973 = recess['1972-11']
rec1973 = rec1973.append(recess['1972-12'])
rec1973 = rec1973.append(x)
rec1973 = rec1973.append(recess['1980-01'])
rec1973 = rec1973.append(recess['1980-02'])
rec1973 = rec1973.append(recess['1980-03'])
rec1973 = rec1973.append(recess['1980-04'])
rec1973 = rec1973.append(recess['1980-05'])
rec1973 = rec1973.append(recess['1980-06'])
rec1973 = rec1973.append(recess['1980-07'])
rec1973 = rec1973.append(recess['1980-08'])
rec1973 = rec1973.append(recess['1980-09'])
rec1973 = rec1973.append(recess['1980-10'])
rec1973 = rec1973.append(recess['1980-11'])

#generating time period of 1969-12 recession
x = recess[(recess['date'].dt.year >= 1969) &
        (recess['date'].dt.year <= 1976)]

rec1969 = recess['1968-12']
rec1969 = rec1969.append(x)

#generating time period of 1960-04 recession
x = recess[(recess['date'].dt.year > 1966) &
        (recess['date'].dt.year < 1968)]
y = recess[(recess['date'].dt.year>2059) & (recess['date'].dt.year<2066)]
rec1960 = recess['2059-04']
rec1960 = rec1960.append(recess['2059-05'])
rec1960 = rec1960.append(recess['2059-06'])
rec1960 = rec1960.append(recess['2059-07'])
rec1960 = rec1960.append(recess['2059-08'])
rec1960 = rec1960.append(recess['2059-09'])
rec1960 = rec1960.append(recess['2059-10'])
rec1960 = rec1960.append(recess['2059-11'])
rec1960 = rec1960.append(recess['2059-12'])
rec1960 = rec1960.append(y)
rec1960 = rec1960.append(x)
rec1960 = rec1960.append(recess['1968-01'])
rec1960 = rec1960.append(recess['1968-02'])
rec1960 = rec1960.append(recess['1968-03'])
rec1960 = rec1960.append(recess['1968-04'])

#generating time period of 1957-08 recession
x = recess[(recess['date'].dt.year > 2056) &
        (recess['date'].dt.year < 2064)]
rec1957 = recess['2056-08']
rec1957 = rec1957.append(recess['2056-09'])
rec1957 = rec1957.append(recess['2056-10'])
rec1957 = rec1957.append(recess['2056-11'])
rec1957 = rec1957.append(recess['2056-12'])
rec1957 = rec1957.append(x)
rec1957 = rec1957.append(recess['2064-01'])
rec1957 = rec1957.append(recess['2064-02'])
rec1957 = rec1957.append(recess['2064-03'])
rec1957 = rec1957.append(recess['2064-04'])
rec1957 = rec1957.append(recess['2064-05'])
rec1957 = rec1957.append(recess['2064-06'])
rec1957 = rec1957.append(recess['2064-07'])
rec1957 = rec1957.append(recess['2064-08'])

#generating time period of 1953-07 recession
x = recess[(recess['date'].dt.year > 2052) &
        (recess['date'].dt.year < 2060)]
rec1953 = recess['2052-07']
rec1953 = rec1953.append(recess['2052-08'])
rec1953 = rec1953.append(recess['2052-09'])
rec1953 = rec1953.append(recess['2052-10'])
rec1953 = rec1953.append(recess['2052-11'])
rec1953 = rec1953.append(recess['2052-12'])
rec1953 = rec1953.append(x)
rec1953 = rec1953.append(recess['2060-01'])
rec1953 = rec1953.append(recess['2060-02'])
rec1953 = rec1953.append(recess['2060-03'])
rec1953 = rec1953.append(recess['2060-04'])
rec1953 = rec1953.append(recess['2060-05'])
rec1953 = rec1953.append(recess['2060-06'])
rec1953 = rec1953.append(recess['2060-07'])

#generating time period of 1948-11 recession
x = recess[(recess['date'].dt.year > 2047) &
        (recess['date'].dt.year < 2055)]
rec1948 = recess['2047-11']
rec1948 = rec1948.append(recess['2047-12'])
rec1948 = rec1948.append(x)
rec1948 = rec1948.append(recess['2055-01'])
rec1948 = rec1948.append(recess['2055-02'])
rec1948 = rec1948.append(recess['2055-03'])
rec1948 = rec1948.append(recess['2055-04'])
rec1948 = rec1948.append(recess['2055-05'])
rec1948 = rec1948.append(recess['2055-06'])
rec1948 = rec1948.append(recess['2055-07'])
rec1948 = rec1948.append(recess['2055-08'])
rec1948 = rec1948.append(recess['2055-09'])
rec1948 = rec1948.append(recess['2055-10'])
rec1948 = rec1948.append(recess['2055-11'])

#generating time period of 1945-02 recession
x = recess[(recess['date'].dt.year > 2044) &
        (recess['date'].dt.year < 2052)]
rec1945 = recess['2044-02']
rec1945 = rec1945.append(recess['2044-03'])
rec1945 = rec1945.append(recess['2044-04'])
rec1945 = rec1945.append(recess['2044-05'])
rec1945 = rec1945.append(recess['2044-06'])
rec1945 = rec1945.append(recess['2044-07'])
rec1945 = rec1945.append(recess['2044-08'])
rec1945 = rec1945.append(recess['2044-09'])
rec1945 = rec1945.append(recess['2044-10'])
rec1945 = rec1945.append(recess['2044-11'])
rec1945 = rec1945.append(recess['2044-12'])
rec1945 = rec1945.append(x)
rec1945 = rec1945.append(recess['2052-01'])
rec1945 = rec1945.append(recess['2052-02'])

#generating time period of 1937-05 recession
rec1937 = recess[(recess['date'].dt.year >= 2036) &
        (recess['date'].dt.year < 2044)]
rec1937 = rec1937.append(recess['2044-01'])
rec1937 = rec1937.append(recess['2044-02'])
rec1937 = rec1937.append(recess['2044-03'])
rec1937 = rec1937.append(recess['2044-04'])
rec1937 = rec1937.append(recess['2044-05'])
rec1937['2037']

#generating time period of 1929-08 recession
rec1929 = recess[(recess['date'].dt.year >= 2028) &
        (recess['date'].dt.year <= 2036)]

#3(b) Normalize
rec2007 = rec2007.divide(138413, axis=1, level=None, fill_value=None)
rec2001 = rec2001.divide(132752, axis=1, level=None, fill_value=None)
rec1990 = rec1990.divide(109830, axis=1, level=None, fill_value=None)
rec1981 = rec1981.divide(91602, axis=1, level=None, fill_value=None)
rec1980 = rec1980.divide(90802, axis=1, level=None, fill_value=None)
rec1973 = rec1973.divide(77912, axis=1, level=None, fill_value=None)
rec1969 = rec1969.divide(71240, axis=1, level=None, fill_value=None)
rec1960 = rec1960.divide(54812, axis=1, level=None, fill_value=None)
rec1957 = rec1957.divide(53126, axis=1, level=None, fill_value=None)
rec1953 = rec1953.divide(50536, axis=1, level=None, fill_value=None)
rec1948 = rec1948.divide(45194, axis=1, level=None, fill_value=None)
rec1945 = rec1945.divide(41904, axis=1, level=None, fill_value=None)
rec1937 = rec1937.divide(30705, axis=1, level=None, fill_value=None)
rec1929 = rec1929.divide(31294, axis=1, level=None, fill_value=None)


#setting common index for data before 1939
np.linspace(15,79,num=65)
x = np.array([-10, 2, 14])
y = np.linspace(15,79,num=65)
x = np.hstack([x,y])
rec1937['xaxis'] = x
rec1929['xaxis'] = [-1, 11, 23, 35, 47, 59, 71, 83]

before1939 = [rec1937, rec1929]
for i in before1939:
    del i['date']
    i.reset_index(drop = True, inplace=True)
    i.set_index('xaxis', inplace = True)

years = [rec2007, rec2001, rec1990, rec1981, rec1980, rec1973, rec1969, rec1960, rec1957, rec1953, rec1948, rec1945]

for i in years:
    i['xaxis']=np.linspace(-12,84,num=97)
    del i['date']
    i.reset_index(drop = True, inplace=True)
    i.set_index('xaxis', inplace = True)

plot = True

if plot:
    '''
    --------------------------------------------------------------------
    cur_path    = string, path name of current directory
    output_fldr = string, folder in current path to save files
    output_dir  = string, total path of images folder
    output_path = string, path of file name of figure to be saved
    xx          = (45,) vector, values of xx
    yy          = (45,) vector, values of yy
    --------------------------------------------------------------------
    '''
    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)
    #3(c)(d) plotting 14 series
    width = 11.5
    height = 6
    fig, ax = plt.subplots(figsize = (width,height))

    plt.plot(rec2007, linestyle=':', color='b', label='2007-12-01')
    plt.plot(rec2001, linestyle='-.', color='g', label='2001-03-01')
    plt.plot(rec1990, linestyle='-.', color='brown', label='1990-07-01')
    plt.plot(rec1981, linestyle='--', color='maroon', label='1981-07-01')
    plt.plot(rec1980, linestyle=':', color='orange', label='1980-01-01')
    plt.plot(rec1973, linestyle='-.', color='red', label='1973-11-01')
    plt.plot(rec1969, linestyle=':', color='k', label='1969-12-01')
    plt.plot(rec1960, linestyle=':', color='black', label='1960-04-01')
    plt.plot(rec1957, linestyle=':', color='pink', label='1957-08-01')
    plt.plot(rec1953, linestyle='-.', color='orange', label='1953-07-01')
    plt.plot(rec1948, linestyle='--', color='pink', label='1948-11-01')
    plt.plot(rec1945, linestyle=':', color='g', label='1945-02-01')
    plt.plot(rec1937, linestyle=':', color='maroon', label='1937-05-01')
    plt.plot(rec1929, linestyle='-.', color='b', label='1929-08-01')

    #3(e) setting legend outside of axes on the right
    plt.legend(bbox_to_anchor=(1.133, 1), loc='upper right', prop={'size':8}, ncol=1)

    #3(f) labelling titles, x-axis and y-axis
    plt.title('Normalized Peak Plot: Job Growth during last 14 Recessions', fontsize=17)
    plt.xlabel(r'Time from peak')
    plt.xlim([-12,86])
    plt.ylabel(r'Jobs/peak')

    #3(g) Labelling x-axis with 9 labels
    my_xticks = ['-1yr','peak','+1yr','+2yr','+3yr','+4yr','+5yr','+6yr','+7yr']
    #creating markers for x-axis labels
    A = []
    i = -12
    while i < 85:
        A.append(i)
        i+=12
    plt.xticks(A, my_xticks )

    #3(h) Plotting reference horizontal and vertical lines
    #creating horizontal line representing jobs/peak = 1
    default = rec2001
    del default['payems']
    default['payems'] = np.array(1)
    plt.plot(default, linestyle='--', color='grey')
    #creating vertical line representing peak
    plt.plot((0.0, 0), (0.0, 1.4), color = 'grey', linestyle ='--')

    #3(i) Red thick solid line plot for Great Recession and black thick solid line plot for Great Depression
    plt.plot(rec2007, linestyle='-', color='red', label='2007-12-01', lw=2)
    plt.plot(rec1929, linestyle='-', color='black', label='1929-08-01', lw = 2)

    output_path = os.path.join(output_dir, 'recessions')
    plt.savefig(output_path)
    # plt.show()
    plt.close()
