import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pandas import Series, DataFrame
from datetime import datetime
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
