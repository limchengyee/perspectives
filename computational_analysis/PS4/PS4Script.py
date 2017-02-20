import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

hr = pd.read_csv('HR_comma_sep.csv')
#explore the differences in characteristics between people that left the company and those who stayed
hr.groupby('left').describe()
#those who left spent less monthly hours than those stayed
#those who left had higher last_evaluation score than those who stayed
#those who left had a much lower average of receiving a promotion over the last five years
#those who left had a lower average satisfication level
#exploring data based on employees that left or stayed

# defining heat map of correlation matrices
def heat_map(corrs_mat):
    sns.set(style="white")
    f, ax = plt.subplots(figsize=(11, 9))
    mask = np.zeros_like(corrs_mat, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corrs_mat, mask=mask, cmap=cmap, ax=ax)
# calculating correlations for the entire dataframe
var_corr = hr.corr()
# visualize correlations between all variables to determine highly correlated variables
heat_map(var_corr)

#plotting and saving graph
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

    #pairwise plot to visualize key characteristics differences between employees that stayed and left
    sns.set(style="whitegrid")

    g = sns.pairplot(hr, hue="left", palette="husl", size=3,
                     vars=['satisfaction_level', 'last_evaluation', 'average_montly_hours', 'promotion_last_5years', 'left'])
    g = g.map(plt.scatter, linewidths=1, edgecolor="w", s=40)
    g = g.add_legend()

    g.fig.suptitle('Plotting pairwise relationships of key characteristics')

    output_path = os.path.join(output_dir, 'pairwise_plot')
    plt.savefig(output_path)
    # plt.show()
    plt.close()
#Conclusions from pairgrid
#Employees that left the organisation have lower satisfaction levels, works high number of hours even though their last evaluations were pretty high.
#Most of the employees that left rarely had a promotion over the last five years.
