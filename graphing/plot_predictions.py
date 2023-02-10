#!/usr/bin/env python3

import matplotlib.pyplot as plt
import csv
import pandas as pd
import argparse
import seaborn as sns
import numpy as np
from statistics import mean


# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=False, default='.', 
        help="path to video frame files default is ./")
ap.add_argument("-f", "--file", required=True, type=str,
	help="file name for pulse data made by find_contours.py")
ap.add_argument("-o", "--outfile", required=False, default='', type=str,
	help="file name for pulse data made by find_contours.py")

args = vars(ap.parse_args())
file = args["file"]
outfile = args["outfile"]
path = args["path"]

#Set class values (probably better to read in a file instead of hard code)
class0min = 340
class0max = 360
class1max = 380
class2max = 420
class3max = 450
class4max = 480
class5max = 490
class6max = 495
class7max = 505
class8max = 520
class9max = 550

#Used a calculator to get hex color from wavelength 
#https://academo.org/demos/wavelength-to-colour-relationship/
class0col = '#0f0f0f'	#350 is UV so using grey 
class1col = '#0f0f0f'	#370 is UV so using grey
class2col = '#8300b5'	#400
class3col = '#2300ff'	#435
class4col = '#0092ff'	#465
class5col = '#00eaff'	#485
class6col = '#00ffe0'	#493
class7col = '#00ff92'	#500
class8col = '#15ff00'	#513
class9col = '#70ff00'	#535

#Read data
table = pd.read_csv(file, delimiter = ',')

#Duplicate predicted class next to change to actual lmax 
table['Predicted_lmax'] = table.loc[:, 'Predicted_Class']

#Convert class values to median lambda max value of that class in new column
table['Predicted_lmax'] = table['Predicted_lmax'].replace(0,mean([class0min,class0max]))
table['Predicted_lmax'] = table['Predicted_lmax'].replace(1,mean([class0max,class1max]))
table['Predicted_lmax'] = table['Predicted_lmax'].replace(2,mean([class1max,class2max]))
table['Predicted_lmax'] = table['Predicted_lmax'].replace(3,mean([class2max,class3max]))
table['Predicted_lmax'] = table['Predicted_lmax'].replace(4,mean([class3max,class4max]))
table['Predicted_lmax'] = table['Predicted_lmax'].replace(5,mean([class4max,class5max]))
table['Predicted_lmax'] = table['Predicted_lmax'].replace(6,mean([class5max,class6max]))
table['Predicted_lmax'] = table['Predicted_lmax'].replace(7,mean([class6max,class7max]))
table['Predicted_lmax'] = table['Predicted_lmax'].replace(8,mean([class7max,class8max]))
table['Predicted_lmax'] = table['Predicted_lmax'].replace(9,mean([class8max,class9max]))

colorby='Score'

#2d
sns.scatterplot(x='Lambda_Max', y='Predicted_lmax', data=table, edgecolor = 'none', color = 'black', s = 20)
plt.xlabel('Known Lambda-max (nm)')
plt.ylabel('Predicted Lambda-max (mean of class in nm)')


#place colored bands behind plot
plt.axhspan(class0min, class0max, facecolor=class0col, alpha=0.05)
plt.axhspan(class0max, class1max, facecolor=class1col, alpha=0.15)
plt.axhspan(class1max, class2max, facecolor=class2col, alpha=0.1)
plt.axhspan(class2max, class3max, facecolor=class3col, alpha=0.1)
plt.axhspan(class3max, class4max, facecolor=class4col, alpha=0.1)
plt.axhspan(class4max, class5max, facecolor=class5col, alpha=0.1)
plt.axhspan(class5max, class6max, facecolor=class6col, alpha=0.1)
plt.axhspan(class6max, class7max, facecolor=class7col, alpha=0.1)
plt.axhspan(class7max, class8max, facecolor=class8col, alpha=0.1)
plt.axhspan(class8max, class9max, facecolor=class9col, alpha=0.1)

##Calculate regression
corr_matrix = np.corrcoef(table.loc[:,'Lambda_Max'], table.loc[:,'Predicted_lmax'])
corr = corr_matrix[0,1]
R_sq = corr**2
print(R_sq)


#If no file name show on screen otherwise save pdf
if outfile == '' :
    plt.show()
else:
    fileout = outfile + '.pdf'
    plt.savefig(fileout)

