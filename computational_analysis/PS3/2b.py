from mpl_toolkits.mplot3d import Axes3D
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

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
