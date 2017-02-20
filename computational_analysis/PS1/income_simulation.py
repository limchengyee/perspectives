# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
import pandas as pd
import scipy.stats as stats
import pylab as pl
from matplotlib.ticker import MultipleLocator
import os

seed = 300
np.random.seed(seed)

def NextYear(t,inc0,incLast,p,g,e,year):
    incNew = (1-p)*(inc0+g*(t-year)) + p*incLast + e
    return incNew

def calcInc(p,g,inc0,errors,year):
    income = [inc0+errors[0]]
    for i in range(1,len(errors)):
        newInc = NextYear(year+i,inc0,income[-1],p,g,errors[i],year)
        income.append(newInc)
    return income

def simInc(sigma=0.1,p=0.2,g=0.03,inc0=80000,year=2018,duration=40,sims=10000):
    inc0 = np.log(inc0)
    errorList = []
    for i in range(sims):
        errorList.append(np.random.normal(scale = 0.1, size=duration))

    incList = []
    for i in range(sims):
        incList.append(calcInc(p,g,inc0,errorList[i],year))

    incList = np.exp(incList)
    incList = pd.DataFrame(incList)
    y = np.arange(2018, 2058)
    incList.columns = y
    return incList


graph = True
...
if graph:

    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    realIncome = simInc()
    plt.plot(realIncome.transpose()[0])
    minorLocator = MultipleLocator(1)
    plt.grid(b=True, which='major', color='0.65', linestyle='-')
    plt.title('One simulated lifetime income path', fontsize=16)
    plt.xlabel(r'Year $t$')
    plt.ylabel(r'Annual income (\$s)')
    plt.xlim((2015, 2060))

    output_path = os.path.join(output_dir, 'Fig_1a')
    plt.savefig(output_path)
    #plt.show()
    plt.close()


# Part (b)

graph = True
...
if graph:

    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    hist_wgts = (1 / 10000) * np.ones(10000)
    num_bins = 50
    h=realIncome[2018]
    hstd = np.std(h)
    hmean = np.mean(h)

    x = np.linspace(50000,120000,100)

    minorLocator = MultipleLocator(1)
    plt.grid(b=True, which='major', color='0.65', linestyle='-')
    plt.hist(realIncome[2018], num_bins, weights=hist_wgts)
    plt.plot(x, stats.norm.pdf(x, loc = hmean, scale = hstd),'r-', lw=5, alpha=0.6, label='norm pdf')
    plt.title('Histogram of first year ($t$=2018) income', fontsize=16)
    plt.xlabel(r'Annual income (\$s)')
    plt.ylabel(r'Percent of students')
    plt.ylim((0, 0.08))

    output_path = os.path.join(output_dir, 'Fig_1b')
    plt.savefig(output_path)
    #plt.show()
    plt.close()

inc_gt100k_pct=0
for i in realIncome[2018]:
    if i > 100000:
        inc_gt100k_pct += 1

print('1b. Percent of students getting more than $100k in first period: ',
      inc_gt100k_pct/10000 * 100, '%')

inc_ls70k_pct=0
for i in realIncome[2018]:
    if i < 70000:
        inc_ls70k_pct += 1

print('1b. Percent of students getting less than $70k in first period: ',
      inc_ls70k_pct/10000 * 100, '%')

# Part (c)

def repayment(income,loan=95000,startYear=2018):
    paid=0.1*income
    paidt = paid.transpose()
    paidList = []
    yearList = []
    countList = []
    for i in paidt:
        cum = 0
        year = startYear
        count = 0
        while cum < loan:
            cum +=paidt[i][year+count]
            count += 1
        paidList.append(cum)
        yearList.append(year+count)
        countList.append(count)

    paymentPeriod = pd.DataFrame([paidList,yearList,countList]).transpose()
    paymentPeriod.columns = ['Amount Paid','Year of Repayment','Number of Years']
    return paymentPeriod

PP = repayment(realIncome)

if graph:

    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    minorLocator = MultipleLocator(1)
    plt.grid(b=True, which='major', color='0.65', linestyle='-')
    plt.hist(PP['Number of Years'],30)
    plt.title('Histogram of years taken to pay off their loans', fontsize=16)
    plt.xlabel(r'Number of Years')
    plt.ylabel(r'Number of Students')
    plt.xlim((8, 15))

    output_path = os.path.join(output_dir, 'Fig_1c')
    plt.savefig(output_path)
    # plt.show()
    plt.close()

pay_off_ten_years = sum(PP["Number of Years"]<=10)

print('1c. Percent of simulations paying off their loan in 10 years: ',
      pay_off_ten_years/10000 * 100, '%')

# Part (d)

realIncome2 = simInc(sigma=0.15,inc0=85000)
PP2 = repayment(realIncome2)

if graph:
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    minorLocator = MultipleLocator(1)
    plt.grid(b=True, which='major', color='0.65', linestyle='-')
    plt.hist(PP2['Number of Years'],30)
    plt.title('Histogram of years taken to pay off their loans', fontsize=16)
    plt.xlabel(r'Number of Years(\$s)')
    plt.ylabel(r'Number of Students')
    plt.xlim((8, 13))
    plt.ylim((0, 9000))

    output_path = os.path.join(output_dir, 'Fig_1d')
    plt.savefig(output_path)
    # plt.show()
    plt.close()

pay_off_ten_years2 = sum(PP2["Number of Years"]<=10)

print('1d. Percent of simulations paying off their loan in 10 years: ',
      pay_off_ten_years2/10000 * 100, '%')
