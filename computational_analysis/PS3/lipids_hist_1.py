import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

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
