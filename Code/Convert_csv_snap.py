# -*- coding: utf-8 -*-
"""
@author: 7sing
"""

import pandas as pd
import numpy as np
import glob as glob
import matplotlib.pyplot as plt

path = 'D:/Folder/...' ## path to the folder where the files are##

csv_files = glob.glob(path + '/*.csv')

Snapshots = len(csv_files) #Snapshots

count = 0

No_of_elements = 73728 ## Total number of elements in the file, 384x192= 73728 ##

Rows = 384

Col = 192

Components = 2

U = np.empty((No_of_elements,))

V = np.empty((No_of_elements,))

U_act = np.empty((Rows,Col,Snapshots))

V_act = np.empty((Rows,Col,Snapshots))

X = np.empty((Snapshots,Rows,Col,Components))

for file in csv_files:
    df = pd.read_csv(file, usecols=['Ucat:0','Ucat:1'])
    U[:] = df['Ucat:0']
    V[:] = df['Ucat:1']
    U_act[:,:,count] = np.reshape(U, (Rows,Col))
    V_act[:,:,count] = np.reshape(V, (Rows,Col))
    count = count + 1


######Reading data into the output variable######


for i in range(0,Snapshots):
    X[i,:,:,0] = U_act[:,:,i]
    X[i,:,:,1] = V_act[:,:,i]



#####Plotting a sample of the data#####


X_axis = range(0,192)
Y_axis = range(0,384)

[X_plot,Y_plot] = np.meshgrid(X_axis,Y_axis)

fig, ax = plt.subplots(1,1)    
ax.contour(X_plot,Y_plot,X[180,:,:,0]) ## use a random number for accessing snapshot as the first index of X ##
